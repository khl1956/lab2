from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms import validators


class PresentationForm(FlaskForm):
    presentation_name = StringField("Name: ", [
        validators.DataRequired("Please enter name of presentation."),
        validators.Length(2, 40, "Name should be from 2 to 40 symbols")
    ])

    presentation_date = DateField("Date: ", [validators.DataRequired("Please enter date of presentation.")])


    submit = SubmitField("Save")