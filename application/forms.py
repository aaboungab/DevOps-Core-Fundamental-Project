from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Series, Review 

class SeriesCheck:
    def __init__(self,message):
        self.message = message

    def __call__(self, form, field):
        all_series = Series.query.all()
        for series in all_series:
            if series.name == field.data:
                raise ValidationError(self.message)

class SeriesForm(FlaskForm):
    name = StringField('Name', 
		validators=[
			DataRequired(),
			SeriesCheck(message='This Series already exsists')])
    submit = SubmitField('Add Series')

class ReviewForm(FlaskForm):
    desc = StringField('Review',
		validators=[
			DataRequired()])
    rating = SelectField('Ratings',
		choices=[
			('5'),('4'),('3'),('2'),('1'), ('0')])
    submit = SubmitField('Add Review')
