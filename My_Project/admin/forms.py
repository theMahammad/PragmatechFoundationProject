from flask_wtf import FlaskForm
from wtforms import  StringField,TextAreaField,SubmitField,FileField

class SuperioritiesForm(FlaskForm):
    img = FileField('super-img')
    title = TextAreaField('super-title')
    content = TextAreaField('super-content')
    button = SubmitField('submit')
class RestaurantsForm(FlaskForm):
    name = StringField('name')
    logo = FileField('logo')
    about = TextAreaField('about')
    button = SubmitField('submit')
class FaqForm(FlaskForm):
    question = TextAreaField('title')
    answer = TextAreaField('answer')
    button = SubmitField('submit')
class RulesForm(FlaskForm):
    title = TextAreaField('title')
    content = TextAreaField('summernote')
    button = SubmitField('submit')