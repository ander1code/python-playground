from django import forms
from .models import Person
from django.core.exceptions import ValidationError
from .utils.validations import *

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("name", "email", "gender")

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def save(self, *args, **kwargs):
        super(PersonForm, self).save(*args, **kwargs)
        print("Successfully created.")

    def clean_name(self):
        return validator_name((self.cleaned_data.get('name') or '').strip())
    
    def clean_email(self):
        return validator_email((self.cleaned_data.get('email') or '').strip())
    
    def clean_gender(self):
        return validator_gender((self.cleaned_data.get('gender') or '').strip())
