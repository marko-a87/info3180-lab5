# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired

class MovieForm(FlaskForm):
    title = StringField('title',validators =[InputRequired()])
    description = TextAreaField("description", validators = [InputRequired()])
    poster = FileField("poster", validators = [FileRequired(), FileAllowed(['jpg', 'png'], 'Movie posters only' )])

