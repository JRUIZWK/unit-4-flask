from platform import release
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class FavSongsForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired()])
  musician = StringField('Musician', validators=[DataRequired()])
  genre = StringField('Genre', validators=[DataRequired()])
  releaseyear = StringField('Release Year', validators=[DataRequired()])
  text = TextAreaField('Text', validators=[DataRequired()])

  submit = SubmitField('Post')