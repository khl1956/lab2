from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms import validators


class HotelForm(FlaskForm):
    hotel_name = StringField("Name: ", [
        validators.DataRequired("Please enter hotel name."),
        validators.Length(2, 20, "Name should be from 2 to 20 symbols")
    ])
    hotel_opened = IntegerField("Hotel open year: ", [
        validators.DataRequired("Please enter the hotel open year."),
        validators.Lenght(4, 4, "Please enter the correct year")
    ])
    hotel_stars = IntegerField("Hotel stars: ", [
        validators.DataRequired("Please enter hotel stars."),
        validators.Length(1, 1, "Stars should be 1 symbol")
    ])
    hotel_type = SelectField('Type', [
    validators.DataRequired("Please enter hotel type.")],
                           choices=[('Hotel', 'hotel'),
                                    ('Appartments', 'apartments'),
                                    ('Hostel', 'hostel')
                                    ])

    submit = SubmitField("Save")

    def check_open_year_on_submit(self):
        return bool(self.hotel_opened.data > 1990)