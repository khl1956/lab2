from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange, Length, Email

class UserForm(FlaskForm):

    user_email = StringField('email', validators=[DataRequired(), Email("Wrong email format")])

    user_name = StringField('name', validators=[DataRequired(), Length(2)])

    user_age = IntegerField('age', validators=[DataRequired(), NumberRange(min=12, max=100)])

    user_university = StringField('university', validators=[DataRequired(), Length(2)])

    submit = SubmitField("Save")

