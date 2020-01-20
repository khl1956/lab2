from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange, Length, ValidationError


class EditMethodForm(FlaskForm):

    def valid(form, field):
        if int(field.data) > 2048:
            raise ValidationError("No more than 2048")

    method_description = StringField('Describe this method:',  validators=[Length(2, 60, "Description couldn't be longer than 60 symbols"), DataRequired("Please enter number of methods.")])

    output_type = StringField('Type of output', validators=[DataRequired(), Length(2, 30, "Type couldn't be longer than 30 symbols")])

    submit = SubmitField("Save")