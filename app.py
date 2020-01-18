from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from Forms.UserForm import UserForm
from Forms.TopicForm import TopicForm
from Forms.PresentationForm import PresentationForm
from Forms.ParticipantForm import ParticipantForm
from Forms.UserFormEdit import UserFormEdit
from Forms.PresentationFormEdit import PresentationFormEdit
from Forms.TopicFormEdit import TopicFormEdit
from Forms.ParticipantFormEdit import ParticipantFormEdit

from sqlalchemy.sql import func
import plotly
import plotly.graph_objs as go

import json

from Forms.UserForm import UserForm

app = Flask(__name__)
app.secret_key = 'key'

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Trouble228@localhost/LABA2'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jqmtgtltfxjxyw:5d4ed79bfdf9814b34a3483aa0bcfd112fae242e1b10692629464e2a72a470ba@ec2-174-129-253-101.compute-1.amazonaws.com:5432/daeiv5k0b4d4pp'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Topic(db.Model):
    tablename = 'Topic'
    topic_name = db.Column(db.String(20), primary_key=True)
    presentation_name = db.Column(db.String(20), db.ForeignKey('Presentation.presentation_name'))


class User(db.Model):
    tablename = 'User'
    user_email = db.Column(db.String(20), primary_key=True)
    user_name = db.Column(db.String(20))
    user_phone = db.Column(db.String(20))
    user_birthday = db.Column(db.Date)

    user_presentation = db.relationship('Presentation')

# New class Hotel
class Hotel(db.Model):
    tablename = 'Hotel'
    hotel_name = db.Column(db.String(20), primary_key=True)
    hotel_opened = db.Column(db.Date)
    hotel_stars = db.Column(db.Integer)
    hotel_type = db.Column(db.String(20))

    user_hotel = db.relationship('User', secondary = 'UserHasHotel')

# new relation many Users have many Hotels
class UserHasHotel(db.Model):
    __tablename__= 'UserHasHotel'
    user_name = db.Column(db.String(20), db.ForeignKey('User.user_name'), primary_key=True)
    hotel_name = db.Column(db.String(20), db.ForeignKey('Hotel.hotel_name'), primary_key=True)


    hotel_name_fk = db.relationship("Hotel", secondary='UserHasHotel')


class association(db.Model):
    __tablename__ = 'associate_table'
    left_name = db.Column(db.String(20), db.ForeignKey('Presentation.presentation_name'), primary_key=True)
    right_name = db.Column(db.String(20), db.ForeignKey('Topic.topic_name'), primary_key=True)


class Presentation(db.Model):
    __tablename__ = 'Presentation'
    presentation_name = db.Column(db.String(20), primary_key=True)
    user_email = db.Column(db.String(20), db.ForeignKey('User.user_email'))
    presentation_date = db.Column(db.Date)

    participant_list_fk = db.relationship("Participant", secondary='associate_table')
    presentation_topic = db.relationship('Topic')


class Participant(db.Model):
    __tablename__ = 'Participant'
    participant_list = db.Column(db.String(20), primary_key=True)
    participant_name = db.Column(db.String(100))

    presentation_name_fk = db.relationship("Presentation", secondary='associate_table')


# создание всех таблиц
db.create_all()



# очистка всех таблиц
db.session.query(association).delete()
db.session.query(Topic).delete()
db.session.query(Presentation).delete()
db.session.query(User).delete()
db.session.query(Hotel).delete()
db.session.query(Participant).delete()


# # # создане объектов
#
# insert into User (user_email, user_name, user_phone, user_birthday) values ('maria@gmail.com', 'Maria', '+380669983855', '1999-4-7');
#
# insert into User (user_email, user_name, user_phone, user_birthday) values ('bob@gmail.com', 'Bob', '+380123456789', '2000-1-20');
#
# insert into User (user_email, user_name, user_phone, user_birthday) values ('kate@gmail.com', 'Kate', '+123456789011', '1998-2-25');
#
# insert into User (user_email, user_name, user_phone, user_birthday) values ('alex@gmail.com', 'Alex', '+380999999999', '1997-2-25');
#
# insert into User (user_email, user_name, user_phone, user_birthday) values ('sam@gmail.com', 'Sam', '+380777777777', '1999-2-1');
#

Maria = User(user_email = 'maria@gmail.com',
             user_name = 'Maria',
             user_phone = '+380669983855',
             user_birthday = "1999-4-7"
             )

Bob = User(user_email = 'bob@gmail.com',
             user_name = 'Bob',
             user_phone = '+380123456789',
             user_birthday = '2000-1-20'
             )

Kate = User(user_email = 'kate@gmail.com',
             user_name = 'Kate',
             user_phone = '+123456789011',
             user_birthday = '1998-2-25'
            )

Alex = User(user_email = 'alex@gmail.com',
             user_name = 'Alex',
             user_phone = '+380999999999',
             user_birthday = '1997-2-25'
            )

Sam = User(user_email = 'sam@gmail.com',
             user_name = 'Sam',
             user_phone = '+380777777777',
             user_birthday = '1999-2-1'
            )

# Hotel
Hilton = Hotel(hotel_name = 'Hilton',
               hotel_opened = 2012,
               hotel_stars = 5,
               hotel_type = 'hotel'
               )

Intercontinental = Hotel(hotel_name = 'Intercontinental',
                         hotel_opened = 2010,
                         hotel_stars = 5,
                         hotel_type = 'hotel'
                         )

Kyiv = Hotel(hotel_name = 'Kyiv',
             hotel_opened = 2000,
             hotel_stars = 3,
             hotel_type = 'appartments'
             )

Youth = Hotel(hotel_name = 'Youth',
              hotel_opened = 2019,
              hotel_stars = 3,
              hotel_type = 'hostel'
              )

Kolos = Hotel(hotel_name = 'Kolos',
              hotel_opened = 2003,
              hotel_stars = 2,
              hotel_type = 'hostel'
              )

# insert into Presentation (presentation_name, user_email, presentation_date) values ('Sales', 'alex@gmail.com', '2020-1-4');
#

Sales = Presentation(presentation_name = 'Sales',
           user_email = 'alex@gmail.com',
           presentation_date = '2020-1-4')

DataBase = Presentation(presentation_name = 'DataBase',
                  user_email = 'bob@gmail.com',
                  presentation_date = '2020-1-8'
                  )

Music = Presentation(presentation_name = 'Music',
                 user_email = 'maria@gmail.com',
                 presentation_date = '2020-1-12'
                 )

Maths = Presentation(presentation_name = 'Maths',
                    user_email = 'alex@gmail.com',
                    presentation_date = '2020-1-29'
                    )

Sports = Presentation(presentation_name = 'Sports',
                 user_email = 'alex@gmail.com',
                 presentation_date = '2020-2-1'
                 )


# insert into Participant (participant_list, participant_name) values ('Science_Maths', 'Alex, Bob');
#

Science_Maths = Participant(participant_list = 'Science_Maths',
               participant_name = 'Alex, Bob'
               )

Art_Music = Participant(participant_list = 'Art_Music',
             participant_name = 'Maria'
             )

Computer_DataBase = Participant(participant_list = 'Computer_DataBase',
                   participant_name = 'Alex, Bob, Sam'
                   )

Business_Sales = Participant(participant_list = 'Business_Sales',
                participant_name = 'Maria'
                )

Math_Maths = Participant(participant_list = 'Math_Maths',
                participant_name = 'Bob, Sam')


# insert into Topic (topic_name, presentation_name) values ('Art', 'Music');
#
# insert into Topic (topic_name, presentation_name) values ('Science', 'Maths');
#
# insert into Topic (topic_name, presentation_name) values ('Math', 'Maths');
#
# insert into Topic (topic_name, presentation_name) values ('Computer', 'DataBase');
#
# insert into Topic (topic_name, presentation_name) values ('Business', 'Sales');

Art = Topic(topic_name = 'Art',
               presentation_name = 'Music'
               )

Science = Topic(topic_name = 'Science',
                  presentation_name = 'Maths'
                  )

Math = Topic(topic_name = 'Math',
                presentation_name = 'Maths'
                )

Computer = Topic(topic_name = 'Computer',
                         presentation_name = 'DataBase'
                         )

Business = Topic(topic_name = 'Business',
                   presentation_name = 'Sales'
                   )


Alex.user_presentation.append(Sales)
Bob.user_presentation.append(DataBase)
Maria.user_presentation.append(Music)
Alex.user_presentation.append(Maths)
Alex.user_presentation.append(Sports)

Music.presentation_topic.append(Art)
Maths.presentation_topic.append(Science)
Maths.presentation_topic.append(Math)
DataBase.presentation_topic.append(Computer)
Sales.presentation_topic.append(Business)

Maths.participant_list_fk.append(Science_Maths)
Music.participant_list_fk.append(Art_Music)
DataBase.participant_list_fk.append(Computer_DataBase)
Sales.participant_list_fk.append(Business_Sales)
Maths.participant_list_fk.append(Math_Maths)


db.session.add_all([Maria, Bob, Kate, Alex, Sam,
                    Hilton, Intercontinental, Kyiv, Youth, Kolos,
                    Sales, DataBase, Music, Maths, Sports,
                    Science_Maths, Art_Music, Computer_DataBase, Business_Sales, Math_Maths,
                    Art, Science, Math, Computer, Business
])

db.session.commit()

@app.route('/show', methods=['GET', 'POST'])
def get_hotel():
    result=db.session.query(Hotel).all()

    return render_template('all_hotel.html'.result=result)


@app.route('/get')
def insert_hotel_get():
    Hilton = Hotel(hotel_name='Hilton',
                   hotel_opened=2012,
                   hotel_stars=5,
                   hotel_type='hotel'
                   )

    Intercontinental = Hotel(hotel_name='Intercontinental',
                             hotel_opened=2010,
                             hotel_stars=5,
                             hotel_type='hotel'
                             )

    Kyiv = Hotel(hotel_name='Kyiv',
                 hotel_opened=2000,
                 hotel_stars=3,
                 hotel_type='appartments'
                 )

    Youth = Hotel(hotel_name='Youth',
                  hotel_opened=2019,
                  hotel_stars=3,
                  hotel_type='hostel'
                  )

    Kolos = Hotel(hotel_name='Kolos',
                  hotel_opened=2003,
                  hotel_stars=2,
                  hotel_type='hostel'
                  )
    db.session.add_all([Hilton, Intercontinental, Kyiv, Youth, Kolos])
    db.session.commit()
    return render_template('success.html')

@app.route('/plot', methods=['GET', 'POST'])
def plot():
    query1 = (
        db.session.query(
            Hotel.hotel_name,
            Hotel.hotel_stars.label('stars')
        )
    ).all()

    hotel_name, hotel_stars = zip(*query1)
    bar = go.Bar(
        x = hotel_name,
        y = hotel_stars
    )

    data = {
        "bar": [bar]
    }
    graphs_json = json.dumps(data, cls = plotly.utils.PlotlyJSONEncoder)

    return render_template('plot.html', graphsJSON=graphs_json)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    query1 = (
        db.session.query(
            User.user_name,
            func.count(Presentation.presentation_name).label('presentation_name')
        ).join(Presentation, User.user_email == Presentation.user_email).
            group_by(User.user_name)
    ).all()

    print(query1)

    query2 = (
        db.session.query(
            Presentation.presentation_name,
            func.count(Topic.topic_name).label('topic_name')
        ).join(Topic, Presentation.presentation_name == Topic.presentation_name).
            group_by(Presentation.presentation_name)
    ).all()

    print(query2)

    user_name, presentation_name = zip(*query1)
    bar = go.Bar(
        x=user_name,
        y=presentation_name
    )

    presentation_name, topic_name = zip(*query2)
    pie = go.Pie(
        labels=presentation_name,
        values=topic_name
    )

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphs_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphs_json)



@app.route('/edit_user/<string:email>', methods=['GET', 'POST'])
def edit_user(email):
    form = UserFormEdit()
    result = db.session.query(User).filter(User.user_email == email).one()

    if request.method == 'GET':

        form.user_name.data = result.user_name
        form.user_email.data = result.user_email
        form.user_birthday.data = result.user_birthday
        form.user_phone.data = result.user_phone


        return render_template('edit_user.html', form=form, form_name=email)
    elif request.method == 'POST':

        result.user_name = form.user_name.data
        result.user_email = form.user_email.data
        result.user_birthday = form.user_birthday.data.strftime("%Y-%m-%d"),
        result.user_phone = form.user_phone.data

        db.session.commit()
        return redirect('/user')


@app.route('/edit_presentation/<string:name>', methods=['GET', 'POST'])
def edit_presentation(name):
    form = PresentationFormEdit()
    result = db.session.query(Presentation).filter(Presentation.presentation_name == name).one()

    if request.method == 'GET':

        form.presentation_name.data = result.presentation_name
        form.presentation_date.data = result.presentation_date


        return render_template('edit_presentation.html', form=form, form_name=name)
    elif request.method == 'POST':

        result.presentation_name = form.presentation_name.data
        result.presentation_date = form.presentation_date.data.strftime("%Y-%m-%d"),

        db.session.commit()
        return redirect('/presentation')



@app.route('/edit_topic/<string:name>', methods=['GET', 'POST'])
def edit_topic(name):
    form = TopicFormEdit()
    result = db.session.query(Topic).filter(Topic.topic_name == name).one()

    if request.method == 'GET':

        form.topic_name.data = result.topic_name


        return render_template('edit_topic.html', form=form, form_name='Edit Topic')
    elif request.method == 'POST':

        result.topic_name = form.topic_name.data

        db.session.commit()
        return redirect('/topic')


@app.route('/edit_participant/<string:name>', methods=['GET', 'POST'])
def edit_participant(name):
    form = ParticipantFormEdit()
    result = db.session.query(Participant).filter(Participant.participant_list == name).one()

    if request.method == 'GET':

        form.participant_list.data = result.participant_list
        form.participant_name.data = result.participant_name


        return render_template('edit_participant.html', form=form, form_name='Edit Participant')
    elif request.method == 'POST':

        result.participant_list = form.participant_list.data
        result.participant_name = form.participant_name.data

        db.session.commit()
        return redirect('/participant')


@app.route('/create_user', methods=['POST', 'GET'])
def create_user():
    form = UserForm()

    if request.method == 'POST':
        new_user = User(
            user_name=form.user_name.data,
            user_birthday=form.user_birthday.data.strftime("%Y-%m-%d"),
            user_email=form.user_email.data,
            user_phone=form.user_phone.data,
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect('/user')
    elif request.method == 'GET':
        return render_template('create_user.html', form=form)


@app.route('/delete_user/<string:email>', methods=['GET', 'POST'])
def delete_user(email):
    result = db.session.query(User).filter(User.user_email == email).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/user')



@app.route('/create_topic', methods=['POST', 'GET'])
def create_topic():
    form = TopicForm()

    if request.method == 'POST':
        new_topic = Topic(
            topic_name=form.topic_name.data,
        )
        db.session.add(new_topic)
        db.session.commit()
        return redirect('/topic')
    elif request.method == 'GET':
        return render_template('create_topic.html', form=form)


@app.route('/delete_topic/<string:name>', methods=['GET', 'POST'])
def delete_topic(name):
    result = db.session.query(Topic).filter(Topic.topic_name == name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/topic')


@app.route('/create_presentation', methods=['POST', 'GET'])
def create_presentation():
    form = PresentationForm()

    if request.method == 'POST':
        new_presentation = Presentation(
            presentation_name=form.presentation_name.data,
            presentation_date=form.presentation_date.data.strftime("%Y-%m-%d")
        )
        db.session.add(new_presentation)
        db.session.commit()
        return redirect('/presentation')
    elif request.method == 'GET':
        return render_template('create_presentation.html', form=form)


@app.route('/delete_presentation/<string:name>', methods=['GET', 'POST'])
def delete_presentation(name):
    result = db.session.query(Presentation).filter(Presentation.presentation_name == name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/presentation')


@app.route('/create_participant', methods=['POST', 'GET'])
def create_participant():
    form = ParticipantForm()

    if request.method == 'POST':
        new_participant = Participant(
            participant_list=form.participant_list.data,
            participant_name=form.participant_name.data
        )
        db.session.add(new_participant)
        db.session.commit()
        return redirect('/participant')
    elif request.method == 'GET':
        return render_template('create_participant.html', form=form)


@app.route('/delete_participant/<string:name>', methods=['GET', 'POST'])
def delete_participant(name):
    result = db.session.query(Participant).filter(Participant.participant_list == name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/participant')




@app.route('/', methods=['GET', 'POST'])
def root():

    return render_template('index.html')

@app.route('/user', methods=['GET'])
def all_peolpe():
    result = db.session.query(User).all()

    return render_template('all_user.html', result=result)


@app.route('/topic', methods=['GET'])
def all_topic():
    result = db.session.query(Topic).all()

    return render_template('all_topic.html', result=result)


@app.route('/presentation', methods=['GET'])
def all_presentation():
    result = db.session.query(Presentation).all()

    return render_template('all_presentation.html', result=result)


@app.route('/participant', methods=['GET'])
def all_participant():
    result = db.session.query(Participant).all()

    return render_template('all_participant.html', result=result)


if __name__ == "__main__":
    app.run()


