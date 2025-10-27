from django import forms
from .models import Person
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from datetime import date
from .utils.validations import *

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'birthday', 'status', 'gender', 'salary']

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def clean_name(self):
        return validate_name(self.cleaned_data.get('name'))

    def clean_email(self):
        return validate_email(self.cleaned_data.get('email'))

    def clean_salary(self):
        return validate_salary(self.cleaned_data.get('salary'))

    def clean_gender(self):
        return validate_gender(self.cleaned_data.get('gender'))

    def clean_birthday(self):
        return validate_birthday(self.cleaned_data.get('birthday'))
        
    """
    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        if not name.strip():
            raise ValidationError("Name is empty.")
        return name.strip()

    def clean_email(self):
        email = self.cleaned_data.get("email", "")
        email = email.strip()
        if not email:
            raise ValidationError("E-mail is empty.")
        EmailValidator(message="Invalid e-mail.")(email)
        if Person.objects.filter(email__iexact=email).exists():
            raise ValidationError("E-mail already registered.")
        return email

    def clean_salary(self):
        salary = self.cleaned_data.get("salary")
        if salary is None:
            raise ValidationError("Salary is empty.")
        if salary < 0:
            raise ValidationError("Invalid salary. Must be a positive number.")
        return salary

    def clean_gender(self):
        gender = self.cleaned_data.get("gender", "")
        gender = gender.strip() if isinstance(gender, str) else gender
        if not gender:
            raise ValidationError("Gender is empty.")
        if gender not in ['M', 'F']:
            raise ValidationError("Invalid gender. Must be 'M' or 'F'.")
        return gender

    def clean_birthday(self):
        birthday = self.cleaned_data.get("birthday")
        if not birthday:
            raise ValidationError("Birthday is empty.")
        today = date.today()
        eighteen_years_ago = today.replace(year=today.year - 18)
        if birthday > eighteen_years_ago:
            raise ValidationError("Must be at least 18 years old.")
        return birthday
    """