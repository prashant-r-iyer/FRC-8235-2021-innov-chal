from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length

class Details(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(2,20)])
    location = StringField('Location', validators=[DataRequired()])
    budget = FloatField('Budget', validators=[DataRequired()])
    bodypart = StringField('Body part to workout', validators=[DataRequired()])
    time = StringField('Workout time', validators=[DataRequired()])
    submit = SubmitField('Ok')