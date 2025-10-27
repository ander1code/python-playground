from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.core.validators import RegexValidator

def validate_name(name):
    if not name:
        raise ValidationError('Name is empty.')
    if len(name) > 1 and len(name) < 5:
        raise ValidationError('Invalid name.')
    
def validate_email(email):
    if not email:
        raise ValidationError('Name is empty.')
    
    validator = EmailValidator(message='Invalid E-mail.')
    try:
        validator(email)
    except ValidationError:
        raise ValidationError('Invalid E-mail.')
    
def validate_gender(gender):
    if not gender:
        raise ValidationError('Gender is empty.')
    
    validator = RegexValidator(
        regex=r'^[MFO]$',
        message='Invalid Gender.'
    )
    validator(gender)


    