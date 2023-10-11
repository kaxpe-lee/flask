from flask_wtf import FlaskForm
from wtforms import DateField,StringField, SubmitField,SelectField, PasswordField, IntegerField, BooleanField, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf.file import FileField, FileRequired

#Formulario de registro
class login(FlaskForm):
    username = StringField('Username:', validators=[DataRequired(), Length(max=45)])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Aceptar')
    
class paso2(FlaskForm):
    step = StringField('step')
    submit = SubmitField('Aceptar')
class paso3(FlaskForm):
    step = StringField('step')
    submit = SubmitField('Aceptar')

class step4(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')

class step5(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')