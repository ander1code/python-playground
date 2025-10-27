from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

def validator_name(name):
    if not name:
        raise ValidationError('Name is empty.')
    return name

def validator_email(email):
    if not email:
        raise ValidationError('E-mail is empty.')
    validator = EmailValidator('Invalid e-mail.')
    validator(email)
    return email

def validator_gender(gender):
    if not gender:
        raise ValidationError('Gender is empty.')
    if not gender in ['M','F']:
        raise ValidationError('Invalid gender.')
    return gender