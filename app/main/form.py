from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Form(FlaskForm):
    User = StringField('Username')
    Password = StringField('Password')
    Submit = SubmitField('Submit')
