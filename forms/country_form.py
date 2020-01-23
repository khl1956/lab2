from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange, Length, ValidationError


class CountryForm(FlaskForm):

    country_name = StringField('country name ', validators=[ DataRequired(), Length(2, 30, "Name should be from 2 to 30 symbols")])

    founding_year = IntegerField('founding year', validators=[DataRequired("Please enter founding year."), NumberRange(min=1000, max=2020)])

    president = StringField('president', validators=[ DataRequired(), Length(2, 60)])

    government_struct = SelectField('government structure', choices=[('democratic','democratic'), ('unitary','unitary')], validators=[DataRequired("Please enter number of methods.")])

    submit = SubmitField("Save")