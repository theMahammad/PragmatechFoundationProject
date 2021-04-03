from flask_wtf import FlaskForm
from wtforms import  StringField,TextAreaField,SubmitField,FileField,PasswordField,BooleanField,validators
from wtforms.fields.html5 import EmailField
class RegistrationForm(FlaskForm):
    fullname = StringField('fullname')
    email = EmailField('email')
    password = PasswordField('password',[validators.DataRequired(),validators.EqualTo('confirm',message = "Şifrələr eyni olmalıdır")])
    confirm= PasswordField('repassword')
    button  = SubmitField('submit')
class LoginForm(FlaskForm):
    email = EmailField('email')
    password = PasswordField('password',[validators.DataRequired()])
    remember = BooleanField('Remember me')
    button  = SubmitField('submit')

    
