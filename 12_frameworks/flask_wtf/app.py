from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    EmailField, 
    BooleanField, 
    RadioField,
    DecimalField, 
    FileField, 
    DateField, 
    TextAreaField, 
    SelectField,
    SubmitField,
)

from wtforms.validators import (
    DataRequired, 
    Length, 
    Email, 
    NumberRange, 
    Regexp, 
    ValidationError,
    Optional
)

from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hasghdahd712562fdsgfgdas'

GENDERS = (
    ('M','Male'),('F','Female'),('O','Other')
)

class PersonForm(FlaskForm):
    name = StringField(label='Name', render_kw={
        "maxlength": 50,    # adicionando caracteristicas, inclusive classes
        "class": 'form-control',
    })
    email = EmailField(label='Email')
    status = BooleanField(label='Status')
    description = TextAreaField(label='Description')
    submit = SubmitField(label='SEND')

    # funciona como clean_<DATA>

    def validate_name(self, field):
        data = field.data # ATENÇÃO: pegar o VALOR, pois É passado o CAMPO!
        if not data or not data.strip():
            raise ValidationError('Name is empty.')
        if len(data) < 4: 
            raise ValidationError('Invalid Name: nome nao pode ter menos que 5 caracteres.')
        if len(data) > 50: 
            raise ValidationError('Invalid Name: nome nao pode ter mais de 50 caracteres.')
        return data

    # funciona como clean_<DATA>
    def validate_email(self, field):

        data = field.data # ATENÇÃO: pegar o VALOR, pois É passado o CAMPO!

        if not data or not data.strip():
            raise ValidationError('E-mail is empty.')
        validator = Email(message='Invalid e-mail.')
        validator(data)
        if True: # consulta no banco se existe!
            raise ValidationError('E-mail is already registered.')
        return data

class NaturalPerson(PersonForm):
    cpf = StringField(label='CPF',)
    birthday = StringField(label='Birthday')
    gender = SelectField(label='Gender', choices=GENDERS)
    salary = StringField(label='Salary')
    picture = FileField(label='pictures', render_kw={
        'disabled':'true',
        'class':'form-control',
    })

    def validate_cpf(self, field):
        
        def validate_cpf_number(cpf):
            return True # metodo para validar cpf!
        
        data = field.data # ATENÇÃO: pegar o VALOR, pois É passado o CAMPO!

        if not data or not data.strip():
            raise ValidationError('CPF is empty.')

        try:
            int(data)
        except:
            raise ValidationError('Invalid CPF number.')

        validator = Regexp(regex=r'^(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$', message='Invalid CPF format.')
        validator(data)
        if validate_cpf_number(data):
            raise ValidationError('Invalid CPF number.')
        if True: # consultar o banco para verificar se cadastrado!
            raise ValidationError('CPF is already registered.')
        return data 

    def validate_birthday(self, field):
        data = field.data # ATENÇÃO: pegar o VALOR, pois É passado o CAMPO!
        if not data or not data.strip():
            raise ValidationError('Birthday is empty.')
        
        import re
        if not re.fullmatch(r'^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{4}$?', data):
            raise ValidationError('Invalid salary format.')

        
        
        today = date.today()
        if data > date(today.year - 18, today.month, today.day):
            raise ValidationError('Invalid birthday: somente acima de 18 anos.')
        return data

    def validate_gender(self, field):
        data = field.data # ATENÇÃO: pegar o VALOR, pois É passado o CAMPO!
        if not data or not data.strip():
            raise ValidationError('Gender is empty.')
        if not data in ['M','F','O']:
            raise ValidationError('Invalid gender.')
        return data

    def validate_salary(self, field):
        data = field.data # ATENÇÃO: pegar o VALOR, pois É passado o CAMPO!
        if not data or not data.strip():
            raise ValidationError('Salary is empty.')

        try:
            float(data)
        except:
            raise ValidationError(' 1- Invalid salary format.')

        validator = Regexp(regex=r'^(?:0|[1-9]\d{0,9})(?:[.,]\d{1,2})?$', message='2 - Invalid salary format.')
        validator(data)
        print('validou!')
        if data < 0:
            raise ValidationError('Invalid Salary: nao pode ser abaixo de 0.')
        if data > 9999999999.99:
            raise ValidationError('Invalid Salary: nao pode ser acima de 9999999999.99.')
        return data


from flask import flash

@app.route("/", methods=['POST','GET'])
def index():
    flash("Successfully created!", "success")
    flash("Error creating!", "danger")
    flash("Warning!", "warning")
    flash("Already logged!", "info")
    form = None
    if request.method == 'POST':
        form = NaturalPerson()
        if form.validate_on_submit():
            return form.data # jogando os dados validos para algum lugar.
        return render_template('form.html', form=form, edition=False)
    form = NaturalPerson()
    return render_template('form.html', form=form, edition=True)

if __name__ == "__main__":
    app.run(debug=True, port=80)



