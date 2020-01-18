from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms.user_form import BuildingForm, UsersForm, LessonForm, BuildingForm1, UsersForm1, LessonForm1, CityForm, CityForm1

import plotly.graph_objs as go
import plotly
import json

import plotly
import json
from flask_sqlalchemy import SQLAlchemy
import plotly.graph_objs as go
from sqlalchemy.sql import func

app = Flask(__name__)
app.secret_key = 'key'

ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1@localhost/laba_2'
else:
    app.debug = False
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgres://fhehffwmvlzkku:e4e9539062e2cd4765550e4ad36e835e630b2d4b442504998f870733d03df2a0@ec2-79-125-2-142.eu-west-1.compute.amazonaws.com:5432/d1jhdnlc95ioeq'



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class ormBuilding(db.Model):
    __tablename__ = 'Building'

    build_number = db.Column(db.String(50), primary_key=True)
    build_address = db.Column(db.String(50), nullable=False)
    floors_number = db.Column(db.String(50), nullable=False)

    Lesson_ = db.relationship('ormLesson')
    city_name = db.relationship('ormCity', secondary='city_has_building')


class ormCity(db.Model):
    __tablename__ = 'City'

    city_name = db.Column(db.String(50), primary_key=True)
    foundation_year = db.Column(db.String(50), nullable=False)
    country_name = db.Column(db.String(50), nullable=False)
    city_mayor = db.Column(db.String(50), nullable=False)

    build_number = db.relationship('ormBuilding', secondary='city_has_building')

class cityHasBuilding(db.Model):
    __tablename__ = 'city_has_building'
    build_number = db.Column(db.String(20), db.ForeignKey('Building.build_number'), primary_key=True)
    city_name = db.Column(db.String, db.ForeignKey('City.city_name'), primary_key=True)



class ormUsers(db.Model):
    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(40), nullable=False)
    user_surname = db.Column(db.String(30), nullable=False)
    user_email = db.Column(db.String(30), nullable=False)
    user_groupe = db.Column(db.String(40), nullable=False)
    user_faculty = db.Column(db.String(40), nullable=False)
    user_course = db.Column(db.String(40), nullable=False)

    lesson_name = db.Column(db.String(20), db.ForeignKey('Lesson.lesson_name'), nullable=False)



class ormLesson(db.Model):
    __tablename__ = 'Lesson'

    lesson_name = db.Column(db.String(20), primary_key=True)
    classroom_number = db.Column(db.String, nullable=False)
    build_number = db.Column(db.String, db.ForeignKey('Building.build_number'), nullable=False)

    Users__ = db.relationship('ormUsers')


db.create_all()

db.session.query(ormUsers).delete()
db.session.query(ormLesson).delete()
db.session.query(ormBuilding).delete()
db.session.query(ormCity).delete()

User1 = ormUsers(user_id = 1, user_name ='Andriy', user_surname ='Hladkiy', user_email ='andriyha98@gmail.com', user_groupe ='KM-63', user_faculty ='FMA', user_course ='4', lesson_name ='matan')
User2 = ormUsers(user_id = 2, user_name ='Ihor', user_surname ='Riasik', user_email ='riasik99@gmail.com', user_groupe ='KM-63', user_faculty ='FMA', user_course ='4', lesson_name ='matan')
User3 = ormUsers(user_id = 3, user_name ='Alex', user_surname ='Buc', user_email ='buc99@gmail.com', user_groupe ='KM-63', user_faculty ='FMA', user_course ='4', lesson_name ='matan')
Building1 =ormBuilding(build_number = '14', build_address='politehnichna 14', floors_number='72')
Building2 =ormBuilding(build_number = '7', build_address='politehnichna 21', floors_number='302')
Building3 =ormBuilding(build_number = '15', build_address='politehnichna 16', floors_number='95')
Lesson1 = ormLesson(lesson_name = 'matan', classroom_number = '95', build_number = '15')
Lesson2 = ormLesson(lesson_name = 'db', classroom_number = '72', build_number = '14')
Lesson3 = ormLesson(lesson_name = 'ekonomika', classroom_number = '302', build_number = '7')
City1 = ormCity(city_name = 'Kiev', foundation_year = '1000', country_name = 'Ukraine', city_mayor = 'Klichko', build_number = '15')
City2 = ormCity(city_name = 'Sokiryani', foundation_year = '1500', country_name = 'Ukraine', city_mayor = 'Ravlik', build_number = '15')
City3 = ormCity(city_name = 'Milan', foundation_year = '850', country_name = 'Italy', city_mayor = 'hz kto', build_number = '15')


Lesson1.Users__.append(User1)
Lesson1.Users__.append(User3)
Lesson1.Users__.append(User2)
Building3.Lesson_.append(Lesson1)
Building1.Lesson_.append(Lesson2)
Building2.Lesson_.append(Lesson3)
Lesson1.Users__.append(User1)
Lesson1.Users__.append(User3)
Lesson1.Users__.append(User2)
db.session.add_all([User1,User2,User3])
db.session.add_all([Building1,Building2,Building3])
db.session.add_all([Lesson1,Lesson2,Lesson3])
db.session.add_all([City1,City2,City3])


db.session.commit()



# main page
@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')


# user pages
@app.route('/user', methods=['GET'])
def users():
    result = db.session.query(ormUsers).all()

    return render_template('users.html', users=result)


@app.route('/new_user', methods=['POST', 'GET'])
def new_user():
    form = UsersForm()

    if request.method == 'POST':
        if form.validate() == True:
            ok = ormUsers(
                user_id=form.user_id.data,
                user_name=form.user_name.data,
                user_surname=form.user_surname.data,
                user_email=form.user_email.data,
                user_groupe=form.user_groupe.data,
                user_faculty=form.user_faculty.data,
                user_course=form.user_course.data,
                lesson_name=form.lesson_name.data
            )
            db.session.add(ok)
            db.session.commit()


            return redirect(url_for('users'))
        else:
            return render_template('ok.html', form=form, form_name="ok")

    elif request.method == 'GET':
        return render_template('user_form.html', form=form, form_name="user form")


@app.route('/edit_user/<string:x>', methods=['GET', 'POST'])
def edit_user(x):
    form = UsersForm1()
    user = db.session.query(ormUsers).filter(ormUsers.user_id == x).one()

    if request.method == 'GET':

        # fill form and send to user
        form.user_id.data = user.user_id
        form.user_name.data = user.user_name
        form.user_surname.data = user.user_surname
        form.user_email.data = user.user_email
        form.user_groupe.data = user.user_groupe
        form.user_faculty.data = user.user_faculty
        form.user_course.data = user.user_course

        return render_template('user_form1.html', form=form, form_name="Edit user")

    else:

        if form.validate() == False:
            user.user_name = form.user_name.data
            user.user_surname = form.user_surname.data
            user.user_email = form.user_email.data
            user.user_groupe = form.user_groupe.data
            user.user_faculty = form.user_faculty.data
            user.user_course = form.user_course.data

            db.session.commit()

            # return redirect('/user')
            return render_template('OK.html')
        else:
            return render_template('user_form1.html', form=form, form_name="Edit user")



@app.route('/delete_user/<string:x>', methods=['GET'])
def delete_user(x):
    result = db.session.query(ormUsers).filter(ormUsers.user_id == x).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('OK.html')


# Building
@app.route('/building', methods=['GET'])
def building():
    result = db.session.query(ormBuilding).all()

    return render_template('building.html', building=result)


@app.route('/new_building', methods=['GET', 'POST'])
def new_building():
    form = BuildingForm()

    if request.method == 'POST':
        if form.validate() == True:
            ok = ormBuilding(
                build_number=form.build_number.data,
                build_address=form.build_address.data,
                floors_number=form.floors_number.data

            )
            db.session.add(ok)
            db.session.commit()

            return redirect(url_for('building'))

        else:
            return render_template('building_form.html', form=form, form_name="building form")
    elif request.method == 'GET':

        return render_template('building_form.html', form=form, form_name="building form")


@app.route('/edit_building/<string:x>', methods=['GET', 'POST'])
def edit_building(x):
    form = BuildingForm1()

    user = db.session.query(ormBuilding).filter(ormBuilding.build_number == x).one()

    if request.method == 'GET':



        form.build_address.data = user.build_address
        form.floors_number.data = user.floors_number
        # form.build_number.data = user.build_number

        return render_template('building_form1.html', form=form, form_name="Edit building")


    else:

        if form.validate() == True:
            # find user

            # update fields from form data
            user.build_address = form.build_address.data
            user.floors_number = form.floors_number.data
            # user.build_number = form.build_number.data

            db.session.commit()

            return redirect(url_for('building'))


        else:

            return render_template('building_form1.html', form=form, form_name="Edit building")


@app.route('/delete_building/<string:x>', methods=['GET'])
def delete_building(x):
    result = db.session.query(ormBuilding).filter(ormBuilding.build_number == x).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('OK.html')


# lessons pages
@app.route('/lesson', methods=['GET'])
def lesson():
    result = db.session.query(ormLesson).all()

    return render_template('lessons.html', lesson=result)


@app.route('/new_lesson', methods=['GET', 'POST'])
def new_lesson():
    form = LessonForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('lessons_form.html', form=form, form_name="New lesson", action="new_lesson")
        else:
            new_user = ormLesson(
                lesson_name=form.lesson_name.data,
                classroom_number=form.classroom_number.data,
                build_number=form.build_number.data,

            )
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('lesson'))

    return render_template('lessons_form.html', form=form, form_name="New lesson", action="new_lesson")


@app.route('/edit_lesson/<string:x>', methods=['GET', 'POST'])
def edit_lesson(x):
    form = LessonForm1()
    user = db.session.query(ormLesson).filter(ormLesson.lesson_name == x).one()

    if request.method == 'GET':

        # fill form and send to user
        form.lesson_name.data = user.lesson_name
        form.classroom_number.data = user.classroom_number
        form.build_number.data = user.build_number

        return render_template('lessons_form1.html', form=form, form_name="Edit lesson")


    elif request.method == 'POST':

        if form.validate() == False:
            # update fields from form data
            user.classroom_number = form.classroom_number.data
            user.build_number = form.build_number.data
            db.session.commit()

            return render_template('ok.html')


        else:
            return render_template('lessons_form1.html', form=form, form_name="Edit lesson")




@app.route('/delete_lesson/<string:x>', methods=['GET'])
def delete_lesson(x):
    result = db.session.query(ormLesson).filter(ormLesson.lesson_name == x).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('OK.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    query1 = (
        db.session.query(
            ormUsers.user_faculty,
            func.count(ormUsers.user_id).label('faculty')
        ).
            group_by(ormUsers.user_faculty)
    ).all()

    query2 = (
        db.session.query(
            ormUsers.lesson_name,
            func.avg(ormUsers.user_id).label('lesson_name')
        ).
            group_by(ormUsers.lesson_name)
    ).all()

    names, skill_counts = zip(*query1)
    bar = go.Bar(
        x=names,
        y=skill_counts
    )

    skills, user_count = zip(*query2)
    pie = go.Pie(
        labels=skills,
        values=user_count
    )

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)


#     =================================================================================================

@app.route('/city', methods=['GET'])
def city():
    result = db.session.query(ormCity).all()

    return render_template('city.html', users=result)


@app.route('/new_city', methods=['POST', 'GET'])
def new_city():
    form = CityForm()

    if request.method == 'POST':
        if form.validate() == True:
            ok = ormUsers(
                city_name=form.city_name.data,
                foundation_year=form.foundation_year.data,
                country_name=form.country_name.data,
                city_mayor=form.city_mayor.data,
                build_number=form.build_number.data,

            )
            db.session.add(ok)
            db.session.commit()


            return redirect(url_for('city'))
        else:
            return render_template('ok.html', form=form, form_name="ok")

    elif request.method == 'GET':
        return render_template('city_form.html', form=form, form_name="city form")


@app.route('/edit_city/<string:x>', methods=['GET', 'POST'])
def edit_city(x):
    form = CityForm1()
    user = db.session.query(ormCity).filter(ormCity.city_name == x).one()

    if request.method == 'GET':

        # fill form and send to user
        form.city_name.data = city.city_name
        form.foundation_year.data = city.foundation_year
        form.country_name.data = city.country_name
        form.city_mayor.data = city.city_mayor


        return render_template('city_form1.html', form=form, form_name="Edit city")

    else:

        if form.validate() == False:
            city.foundation_year = form.foundation_year.data
            city.country_name = form.country_name.data
            city.city_mayor = form.city_mayor.data

            db.session.commit()

            # return redirect('/user')
            return render_template('OK.html')
        else:
            return render_template('city_form1.html', form=form, form_name="Edit city")


@app.route('/delete_city/<string:x>', methods=['GET'])
def delete_city(x):
    result = db.session.query(ormCity).filter(ormCity.city_name == x).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('OK.html')



if __name__ == '__main__':
    app.run(debug=True)
