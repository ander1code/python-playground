from django import forms
from .models import Person
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['email'].required = False
        # self.fields['created_at'].required = False

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise ValidationError("Name is empty.")
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip()
        if not email:
            raise ValidationError("E-mail is empty.")
        
        validator = EmailValidator("Invalid E-mail.")
        validator(email)

        # Validação de unicidade (caso você queira garantir aqui também)
        if Person.objects.filter(email=email).exists():
            raise ValidationError("E-mail already registered.")

        return email
    