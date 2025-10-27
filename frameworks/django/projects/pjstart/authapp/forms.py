from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=False)
    password = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput)

    
    """
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['password'].required = False
    """

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        errors = {}
        
        if not username:
            errors['username']  = 'Username is empty.'
        if not password:
            errors['password']  = 'Password is empty.'


        if len(username) >= 1 and len(username) < 8:
            errors['username']  = 'Invalid Username.'

        if len(password) >= 1 and len(password) < 8:
            errors['password']  = 'Invalid Password.'
            
        if errors:
            raise ValidationError(errors)
        
        return self.cleaned_data
            
