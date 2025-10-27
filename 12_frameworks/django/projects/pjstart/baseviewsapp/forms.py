from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


def validator_name(value):
    if not value:
        raise ValidationError('Name is empty.')
    if not value.replace(" ", "").isalpha():
        raise ValidationError('Invalid name. Only letters and spaces are allowed.')


email_validator = EmailValidator(
    message='Invalid E-mail.',
    code='invalid_email'
)


def validator_email(value):
    if not value:
        raise ValidationError('E-mail is empty.')
    try:
        email_validator(value)
    except ValidationError:
        raise ValidationError('Invalid E-mail.')


class PersonForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, validators=[validator_name])
    email = forms.CharField(max_length=50, required=True, validators=[validator_email])
    
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['email'].required = False
    
