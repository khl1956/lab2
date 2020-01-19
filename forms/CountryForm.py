from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms import validators


class CountryForm(FlaskForm):
    country_name = StringField("Name: ", [
        validators.DataRequired("Please enter country name."),
        validators.Length(3, 30, "Name should be from 3 to 30 symbols")
    ])
    country_create = IntegerField("Country create: ", [
        validators.DataRequired("Please enter country create year."),
        # validators.Length(4, 4, "Create year should be from 1000")
    ])
    country_president = StringField("President: ", [
        validators.DataRequired("Please enter President."),
        validators.Length(1, 1000, "Name should be from 1 to 1000 symbols")
    ])

    country_type = SelectField('Type', [
        validators.DataRequired("Please enter country type.")],
                               choices=[('Unitary', 'unitary'),
                                        ('Republic', 'republic')
                                        ])
    submit = SubmitField("Save")

    def check_create_year_on_submit(self):
        return bool(self.country_create.data > 1000)
