from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, HiddenField
from wtforms import validators


class PresentationFormEdit(FlaskForm):
    presentation_name = HiddenField("Name: ", [validators.Length(2, 40, "Name should be from 2 to 40 symbols")])
    presentation_date = DateField("Date: ")


    submit = SubmitField("Save")