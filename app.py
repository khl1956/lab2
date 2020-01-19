from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from forms.CountryForm import CountryForm
import plotly
import plotly.graph_objs as go
import json

app = Flask(__name__)
app.secret_key = 'key'

# ENV = 'dev'

# if ENV == 'dev':
#     app.debug = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost'
# else:
app.debug = False
app.config['SECRET_KEY'] = 'laboratory2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mjmxekekolllgi:906b53d31abc57cf4f389ea7d7546ade4af39dcaded44afb9a8ee8c99cc1f68f@ec2-174-129-33-19.compute-1.amazonaws.com:5432/damp2mcuqj7s40'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class UserHasCountry(db.Model):
    __tablename__ = 'user_has_country'
    country_name = db.Column(db.String(20), db.ForeignKey('country.country_name'), primary_key=True)
    user_email = db.Column(db.String(20), db.ForeignKey('user.user_email'), primary_key=True)


class User(db.Model):
    tablename = 'user'
    user_email = db.Column(db.String(50), primary_key=True)
    user_name = db.Column(db.String(20))

    country_name_fk = db.relationship("Country", secondary='user_has_country')


class Country(db.Model):
    __tablename__ = 'country'
    country_name = db.Column(db.String(20), primary_key=True)
    country_create = db.Column(db.Integer)
    country_president = db.Column(db.String(30))
    country_type = db.Column(db.String(30))

    user_email_fk = db.relationship('User', secondary='user_has_country')


# CREATE tables
db.create_all()

# DROP tables
db.session.query(UserHasCountry).delete()
db.session.query(Country).delete()
db.session.query(User).delete()

# Fill tables
ukraine = Country(country_name='Ukraine',
                  country_president='Zelenskii',
                  country_type='Unitary',
                  country_create=1991
                  )

germany = Country(country_name='Germany',
                  country_president='Merkel',
                  country_type='Unitary',
                  country_create=1990
                  )

poland = Country(country_name='Poland',
                 country_president='Duda',
                 country_type='Unitary',
                 country_create=966
                 )

england = Country(country_name='England',
                  country_president='Johnson',
                  country_type='Republic',
                  country_create=1707
                  )

portugal = Country(country_name='Portugal',
                   country_president='Rebelu',
                   country_type='Unitary',
                   country_create=1143
                   )

qqq = User(user_email='qqq@gmail.com',
           user_name='qqq',
           )

www = User(user_email='www@gmail.com',
           user_name='www',
           )

eee = User(user_email='eee@gmail.com',
           user_name='eee',
           )

rrr = User(user_email='rrr@gmail.com',
           user_name='rrr',
           )

ttt = User(user_email='ttt@gmail.com',
           user_name='ttt',
           )

yyy = User(user_email='yyy@gmail.com',
           user_name='yyy',
           )

qqq.country_name_fk.append(ukraine)
www.country_name_fk.append(poland)
eee.country_name_fk.append(portugal)
rrr.country_name_fk.append(england)
ttt.country_name_fk.append(germany)
yyy.country_name_fk.append(ukraine)

db.session.add_all([qqq, www, eee, rrr, ttt, yyy,
                    ukraine, germany, poland, england, portugal,
                    ])

db.session.commit()


# GET METHOD
@app.route('/get')
def insert_countries_get():
    Ukr = Country(
        country_name='Ukr',
        country_president='Slobodianiuk',
        country_type='Unitary',
        country_create=1991
    )
    Rus = Country(
        country_name='Russian',
        country_president='Putin',
        country_type='Republic',
        country_create=1991
    )
    USA = Country(
        country_name='USA',
        country_president='Trump',
        country_type='Republic',
        country_create=1776
    )
    db.session.add_all([Ukr, Rus, USA])
    db.session.commit()
    return render_template('success.html')


# SHOW
@app.route('/show', methods=['GET', 'POST'])
def get_country():
    result = db.session.query(Country).all()

    return render_template('all_country.html', result=result)


# INSERT
@app.route('/insert', methods=['GET', 'POST'])
def insert_countries():
    form = CountryForm()

    if request.method == 'POST':
        print('asd')

        if form.validate() and form.check_create_year_on_submit():

            new_country = Country(
                country_name=form.country_name.data,
                country_create=form.country_create.data,
                country_president=form.country_president.data,
                country_type=form.country_type.data,
            )
            print('test')
            db.session.add(new_country)
            db.session.commit()
            return redirect('/')
        else:
            if not form.check_create_year_on_submit():
                form.country_create.errors = ['country create year must be > 1000']
            return render_template('country_insert_form.html', form=form)
    else:
        return render_template('country_insert_form.html', form=form)


@app.route('/bar', methods=['GET', 'POST'])
def plot():
    query1 = (db.session.query(Country.country_type, Country.country_name)).all()

    country_type, country_name = zip(*query1)
    print(country_type)
    bar = go.Histogram(x=country_type, y=country_name)

    data = {"bar": [bar]}
    graphs_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('bar.html', graphsJSON=graphs_json)


@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
