from ..models import Person
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from datetime import date

def validate_name(name):
    if not name.strip():
        raise ValidationError("Name is empty.")
    return name.strip()

def validate_email(email):
    email = email.strip()
    if not email:
        raise ValidationError("E-mail is empty.")
    EmailValidator(message="Invalid e-mail.")(email)
    if Person.objects.filter(email__iexact=email).exists():
        raise ValidationError("E-mail already registered.")
    return email

def validate_salary(salary):
    if salary is None:
        raise ValidationError("Salary is empty.")
    if salary < 0:
        raise ValidationError("Invalid salary. Must be a positive number.")
    return salary

def validate_gender(gender):
    if not gender:
        raise ValidationError("Gender is empty.")
    if gender not in ['M', 'F']:
        raise ValidationError("Invalid gender. Must be 'M' or 'F'.")
    return gender

def validate_birthday(birthday):
    if not birthday:
        raise ValidationError("Birthday is empty.")
    today = date.today()
    eighteen_years_ago = today.replace(year=today.year - 18)
    if birthday > eighteen_years_ago:
        raise ValidationError("Must be at least 18 years old.")
    return birthday
