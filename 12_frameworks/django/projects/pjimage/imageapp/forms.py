from django import forms
from datetime import date

class MyForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    birthday = forms.DateField(
        required=True,
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder':'DD/MM/AAAA'}),
        input_formats=['%d/%m/%Y']
    )
    picture = forms.ImageField(required=True)

    def clean_birthday(self):
        birthday = self.cleaned_data['birthday']
        age = (date.today() - birthday).days # verificando pelos dias, se a diferença entre as datas é de 18 anos.
        if age < 18:
            raise forms.ValidationError("Invalid age (birthday).")
        return birthday




