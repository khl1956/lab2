from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask import Flask

app = Flask(__name__)
# подключение
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Trouble228@localhost/LABA2'
# связь
db = SQLAlchemy(app)


app.secret_key = 'development key'

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