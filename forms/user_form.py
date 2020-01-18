from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, DateField, HiddenField, IntegerField,ValidationError
from wtforms import validators


class BuildingForm(Form):
    build_number = StringField("build number: ", [
        validators.DataRequired("Please enter build number."),
        validators.Length(1, 20, "Name should be from 5 to 20 symbols")
    ])

    build_address = StringField("build adress: ", [
        validators.DataRequired("Please enter build adress."),
        validators.Length(1, 20, "Name should be from 5 to 20 symbols")
    ])

    floors_number = StringField("floors number: ", [
        validators.DataRequired("Please enter floors number."),
        validators.Length(1, 20, "Name should be from 5 to 20 symbols")
    ])

    submit = SubmitField("Save")

class BuildingForm1(Form):
    # build_number = StringField("build number: ", [
    #     validators.DataRequired("Please enter build number."),
    #     validators.Length(1, 20, "Name should be from 5 to 20 symbols")
    # ])

    build_address = StringField("build adress: ", [
        validators.DataRequired("Please enter build adress."),
        validators.Length(1, 20, "Name should be from 5 to 20 symbols")
    ])

    floors_number = StringField("floors number: ", [
        validators.DataRequired("Please enter floors number."),
        validators.Length(1, 20, "Name should be from 5 to 20 symbols")
    ])

    submit = SubmitField("Save")

class UsersForm(Form):
    user_id = IntegerField("user id: ", [
        validators.DataRequired("Please enter user id.")
    ])

    user_name = StringField("user name: ", [
        validators.DataRequired("Please enter user name."),
        validators.Length(1, 20, "Name should be from 3 to 20 symbols")
    ])

    user_surname = StringField("user surname: ", [
        validators.DataRequired("Please enter user surname."),
        validators.Length(1, 20, "Name should be from 3 to 20 symbols")])

    user_email = StringField("user email: ", [
        validators.Email("Please enter user_email."),
        validators.Length(1, 40, "Name should be from 5 to 40 symbols")])

    user_groupe = StringField("user groupe: ", [
        validators.DataRequired("Please enter your user_groupe."),
        validators.Length(1, 30, "Name should be from 10 to 30 symbols")])

    user_faculty = StringField("user faculty: ", [
        validators.DataRequired("Please enter user faculty.")])

    user_course = StringField("user course: ", [
        validators.DataRequired("Please enter user course."),
        validators.Length(1, 40, "Name should be from 10 to 40 symbols")
    ])

    lesson_name = StringField("lesson name: ", [
        validators.DataRequired("Please enter lesson name."),
        validators.Length(1, 40, "Name should be from 10 to 40 symbols")
    ])

    submit = SubmitField("Save")


class UsersForm1(Form):
    user_id = IntegerField("user id: ", [
        validators.DataRequired("Please enter user id.")
    ])


    user_name = StringField("user name: ", [
        validators.DataRequired("Please enter user name."),
        validators.Length(1, 20, "Name should be from 3 to 20 symbols")
    ])

    user_surname = StringField("user surname: ", [
        validators.DataRequired("Please enter user surname."),
        validators.Length(1, 20, "Name should be from 3 to 20 symbols")])

    user_email = StringField("user email: ", [
        validators.Email("Please enter user_email."),
        validators.Length(1, 40, "Name should be from 5 to 40 symbols")])

    user_groupe = StringField("user groupe: ", [
        validators.DataRequired("Please enter your user_groupe."),
        validators.Length(1, 30, "Name should be from 10 to 30 symbols")])

    user_faculty = StringField("user faculty: ", [
        validators.DataRequired("Please enter user faculty.")])

    user_course = StringField("user course: ", [
        validators.DataRequired("Please enter user course."),
        validators.Length(1, 40, "Name should be from 10 to 40 symbols")
    ])

    lesson_name = StringField("lesson name: ", [
        validators.DataRequired("Please enter lesson name."),
        validators.Length(1, 40, "Name should be from 10 to 40 symbols")
    ])

    submit = SubmitField("Save")


class LessonForm(Form):
    lesson_name = StringField("lesson name: ", [
        validators.DataRequired("Please enter lesson name."),
        validators.Length(1, 20, "Name should be from 3 to 20 symbols")
    ])

    classroom_number = StringField("classroom number: ", [
        validators.DataRequired("Please enter count items.")
    ])

    build_number = StringField("build number: ", [
        validators.DataRequired("Please enter build_number.")
    ])

    submit = SubmitField("Save")


class LessonForm1(Form):
    lesson_name = StringField("lesson name: ", [
        validators.DataRequired("Please enter lesson name."),
        validators.Length(1, 20, "Name should be from 3 to 20 symbols")
    ])

    classroom_number = StringField("classroom number: ", [
        validators.DataRequired("Please enter count items.")
    ])

    build_number = StringField("build number: ", [
        validators.DataRequired("Please enter build_number.")
    ])

    submit = SubmitField("Save")



def valid(form, field):
    if (field.data) not in ['Ukraine','Italy','Austria']:
        raise ValidationError("input Ukraine,Italy,Austria")

def valid1(form, field):
    if int(field.data) < 1020:
        raise ValidationError("1020 and more")


class CityForm(Form):
    city_name = StringField("city_name: ", [
        validators.DataRequired("Please enter city_name.")
    ])

    foundation_year = StringField("foundation_year: ", [valid1,
        validators.DataRequired("Please enter foundation_year."),
        validators.Length(1, 20, "Name should be from 1 to 20 symbols")
    ])

    country_name = StringField("country_name: ", [valid,
        validators.DataRequired("Please enter country_name."),
        validators.Length(1, 20, "Name should be from 1 to 20 symbols")])

    city_mayor = StringField("city_mayor: ", [
        validators.DataRequired("Please enter city_mayor."),
        validators.Length(1, 40, "Name should be from 1 to 40 symbols")])

    # build_number = StringField("build_number: ", [
    #     validators.DataRequired("Please enter your build_number."),
    #     validators.Length(1, 30, "Name should be from 1 to 30 symbols")])



    submit = SubmitField("Save")


class CityForm1(Form):
    city_name = StringField("city_name: ", [
        validators.DataRequired("Please enter city_name.")
    ])


    foundation_year = StringField("foundation_year: ", [valid1,
        validators.DataRequired("Please enter foundation_year."),
        validators.Length(1, 20, "Name should be from 1 to 20 symbols")
    ])

    country_name = StringField("country_name: ", [valid,
        validators.DataRequired("Please enter country_name."),
        validators.Length(1, 20, "Name should be from 1 to 20 symbols")])

    city_mayor = StringField("city_mayor: ", [
        validators.DataRequired("Please enter city_mayor."),
        validators.Length(1, 40, "Name should be from 1 to 40 symbols")])


    submit = SubmitField("Save")

