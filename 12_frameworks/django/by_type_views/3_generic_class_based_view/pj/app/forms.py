from django import forms
from .models import NaturalPerson
from .utils.validators import Validators

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter a password.'
        }
    ))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
    
    def clean_username(self):
        data = self.cleaned_data["username"]
        return Validators().validate_username(data)
    
    def clean_password(self):
        data = self.cleaned_data["password"]
        return Validators().validate_password(data)

class NaturalPersonSearchForm(forms.Form):

    search = forms.CharField(required=False)
    
class NaturalPersonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NaturalPersonForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def clean_name(self):
        data = self.cleaned_data["name"]
        return Validators().validate_name(data)
    
    def clean_email(self):
        data = self.cleaned_data["email"]
        return Validators().validate_email(data)
    
    def clean_birthday(self):
        data = self.cleaned_data["birthday"]
        return Validators().validate_birthday(data)
    
    def clean_gender(self):
        data = self.cleaned_data["gender"]
        return Validators().validate_gender(data)
    
    def clean_salary(self):
        data = self.cleaned_data["salary"]
        return Validators().validate_salary(data)
    
    def clean_picture(self):
        data = self.cleaned_data["picture"]
        return Validators().validate_picture(data)
    
    class Meta:
        model = NaturalPerson
        fields = ("name", "email", "birthday", "gender", "salary", "picture")
        





