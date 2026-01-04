from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, RegexValidator

class Validators(object):
    __instance = None   

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Validators, cls).__new__(cls)
        return cls.__instance
   
    def validate_name(self, name):
        if not name or not name.split():
            raise ValidationError('Name is empty.')
        if len(name) < 4:
            raise ValidationError('Name must have at least 4 characters.')
        if len(name) > 50:
            raise ValidationError('Name must have at most 50 characters.')
        return name

    def validate_email(self, email, instance=None):
        if not email or not email.split():
            raise ValidationError('E-mail is empty.')
        if len(email) < 6:
            raise ValidationError('E-mail must have at least 6 characters.')
        if len(email) > 50:
            raise ValidationError('E-mail must have at most 50 characters.')
        validator = EmailValidator(message='Invalid format e-mail.')
        validator(email)
        print(instance)
        if instance is not None: 
            from app.models import Person 
            person = Person.objects.filter(email__iexact=email).first() 
            if person and person.pk != instance.pk: 
                raise ValidationError('E-mail is already registered.')
        return email    

    def validate_birthday(self, birthday):
        from datetime import date
        if birthday is None:
            raise ValidationError('Birthday is empty.')
        # ***
        if not isinstance(birthday, date):
            raise ValidationError('Invalid birthday: must be a date object.')
        # ***
        today = date.today()
        if birthday > date(today.year - 18, today.month, today.day):
            raise ValidationError('Invalid birthday: only people over 18 years old can be registered.')
        return birthday

    def validate_gender(self, gender):
        if not gender:
            raise ValidationError('Gender is empty.')
        if len(gender) != 1:
            raise ValidationError('Gender must have only 1 character.')
        if not gender in ['M','F','O']:
            raise ValidationError('Invalid gender. Must be M, F, or O.')
        return gender

    def validate_salary(self, salary):
        if salary is None:
            raise ValidationError('Salary is empty.')
        if salary < 0:
            raise ValidationError('Invalid salary: Salary must be major 0.00.')
        if salary > 9999999999.99:
            raise ValidationError('Invalid salary: Salary must be less 9999999999.99.')
        return salary
    
    def validate_picture(self, picture):
        if picture is None:
            raise ValidationError('Picture is empty.')
        return picture

    def validate_username(self, username):
        if not username or not username.split():
            raise ValidationError('Username is empty.')
        return username
    
    def validate_password(self, password):
        if not password or not password.split():
            raise ValidationError('Password is empty.')
        validator = RegexValidator(regex=r'^\S+$', message='Invalid password format.')
        validator(password)
        return password