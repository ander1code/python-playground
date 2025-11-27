from flask import Flask, render_template, request

# import form class
from flask_wtf import FlaskForm

# import types
from wtforms import StringField, SubmitField

# import validators
from wtforms.validators import DataRequired

# --------------------------------

class PersonForm(FlaskForm):
    name = StringField(
        validators=[DataRequired(message='Name is empty.')],
    )
    submit = SubmitField('SEND')

# --------------------------------

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'yqwyuefqwgfdasgdas17627'

@app.errorhandler(404)
def error_404():
    return 'Page not found!'

@app.errorhandler(500)
def error_500():
    return 'Internal server error!'

@app.route("/", methods=['POST','GET'])
def index():
    form = None
    name = None
    if request.method == 'POST':
        form = PersonForm()
        if form.validate_on_submit():
            name = form.name.data
        return render_template("form.html", form=form, name=name)
    form = PersonForm()
    return render_template("form.html", form=form, name=name)

if __name__ in "__main__":
    app.run(debug=True, port=80)