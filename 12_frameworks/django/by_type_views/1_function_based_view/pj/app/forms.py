from django import forms
from .models import NaturalPerson
from .utils.validators import Validators

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return Validators().validate_username(username)
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        return Validators().validate_password(password)

class NaturalPersonSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)
    
class NaturalPersonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # inicializa os campos
        for field in self.fields.values():
            field.required = False
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        return Validators().validate_name(name)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        return Validators().validate_email(email=email, instance=self.instance)
    
    def clean_birthday(self):
        birthday = self.cleaned_data["birthday"]
        return Validators().validate_birthday(birthday)
    
    def clean_gender(self):
        gender = self.cleaned_data["gender"]
        return Validators().validate_gender(gender)
    
    def clean_salary(self):
        salary = self.cleaned_data["salary"]
        return Validators().validate_salary(salary)
    
    def clean_picture(self):
        picture = self.cleaned_data["picture"]
        return Validators().validate_picture(picture)

    class Meta:
        model = NaturalPerson
        fields = ("name", "email", "birthday", "gender", "salary", "picture")

   
    
