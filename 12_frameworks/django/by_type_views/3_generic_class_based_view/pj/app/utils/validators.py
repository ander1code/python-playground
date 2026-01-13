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
            raise ValidationError('Name must have more than 4 characters.')
        if len(name) > 50:
            raise ValidationError('Name must have less than 50 characters.')
        return name

    def validate_email(self, email, instance=None):
        if not email or not email.split():
            raise ValidationError('E-mail is empty.')
        if len(email) < 6:
            raise ValidationError('E-mail must have more than 6 characters.')
        if len(email) > 50:
            raise ValidationError('E-mail must have less than 50 characters.')
        validators = EmailValidator(message='Invalid E-mail format.')
        validators(email)
        if not instance is None:
            from app.models import Person
            person = Person.objects.filter(email__iexact=email).first()
            if not person is None and person.pk != instance.pk:
                raise ValidationError('This E-mail is already registered.')
        return email

    def validate_birthday(self, birthday):
        from datetime import date
        if birthday is None:
            raise ValidationError('Birthday is empty.')
        if not isinstance(birthday, date):
            raise ValidationError('Invalid format birthday.')
        today = date.today()
        if birthday > date(today.year - 18, today.month, today.day):
            raise ValidationError('You must be at least 18 years old to register."')
        return birthday

    def validate_gender(self, gender):
        if gender is None:
            raise ValidationError('Gender is empty.')
        if len(gender) != 1:
            raise ValidationError('Gender must have 1 character.')
        if not gender in ['M','F','O']:
            raise ValidationError('Invalid gender.')
        return gender

    def validate_salary(self, salary):
        if salary is None:
            raise ValidationError('Salary is empty.')
        if salary < 0:
            raise ValidationError('Salary must be a positive number.')
        if salary > 9999999999.99:
            raise ValidationError('Salary exceeds the maximum allowed value.')
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
        validator = RegexValidator(regex=f'^\S+$', message='Invalid password format.')
        validator(password)
        return password


