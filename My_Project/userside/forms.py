from flask_wtf import FlaskForm
from wtforms import  StringField,TextAreaField,SubmitField,FileField,PasswordField,BooleanField,SelectField,validators
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
class FeedbackForm(FlaskForm):
    restaurant = StringField('restaurant-name')
    serviceRating = SelectField('service')
    tasteRating = SelectField('taste')
    atmosphereRating = SelectField('atmosphere')
    topic = StringField('topic')
    content = TextAreaField('content')
    photo = FileField('photo')


    
