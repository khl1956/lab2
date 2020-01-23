from flask import Flask, render_template, request, redirect
from forms.user_form import UserForm
from forms.edit_user_form import EditUserForm
from forms.parameter_form import ParameterForm
from forms.edit_parameter_form import EditParameterForm
from forms.edit_class_form import EditClassForm
from forms.edit_class_form import EditClassForm
from forms.country_form import CountryForm
from forms.method_form import MethodForm
from forms.edit_method_form import EditMethodForm
import uuid
import json
import plotly
from sqlalchemy.sql import func
import plotly.graph_objs as go
from flask_sqlalchemy import SQLAlchemy
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import random as rnd
from math import fabs

from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans


app = Flask(__name__)
app.secret_key = 'key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vkntpqzmequvzy:d0cfa0ace686dbc41dd553bd05555159211f45db3571ab404cac94be19047fa8@ec2-174-129-254-231.compute-1.amazonaws.com:5432/dbm1daba6oq9rk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:fastdagger@localhost/milev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class OrmUser(db.Model):
    __tablename__ = 'user'
    user_email = db.Column(db.String(45), primary_key=True)
    user_name = db.Column(db.String(25), nullable=False)
    user_age = db.Column(db.Integer, nullable=False)
    user_university = db.Column(db.String(25), nullable=False)
    country_ = db.relationship('OrmCountry', secondary='user_lives_country')
    class_ = db.relationship('OrmClass')


class OrmCountry(db.Model):
    __tablename__ = 'country'
    country_name = db.Column(db.String(45), primary_key=True)
    founding_year = db.Column(db.Integer, nullable=False)
    president = db.Column(db.Integer, nullable=False)
    government_struct= db.Column(db.String(25), nullable=False)

    user_email = db.relationship('OrmUser', secondary='user_lives_country')


class user_lives_country(db.Model):
    __tablename__ = 'user_lives_country'
    user_email = db.Column(db.String(45), db.ForeignKey('user.user_email'), primary_key=True)
    country_name = db.Column(db.String(45), db.ForeignKey('country.country_name'), primary_key=True)



class OrmClass(db.Model):
    __tablename__ = 'class'
    class_name = db.Column(db.String(30), primary_key=True)
    methods_quantity = db.Column(db.Integer, nullable=False)
    class_description = db.Column(db.String(50), nullable=True)
    user_email = db.Column(db.String(45), db.ForeignKey('user.user_email'), nullable=False)

    method_ = db.relationship('OrmMethod')


class OrmMethod(db.Model):
    __tablename__ = 'method'
    method_name = db.Column(db.String(30), primary_key=True)
    method_description = db.Column(db.String(50), nullable=False)
    memory_size = db.Column(db.Integer, nullable=False)
    output_type = db.Column(db.String(50), nullable=False)
    class_name = db.Column(db.String(30), db.ForeignKey('class.class_name'), nullable=False)

    parameter_ = db.relationship('OrmParameter')

class OrmParameter(db.Model):
    __tablename__ = 'parameter'

    parameter_name = db.Column(db.String(30), primary_key=True)
    parameter_description = db.Column(db.String(50), nullable=False)
    parameter_type = db.Column(db.String(25), nullable=False)
    method_name = db.Column(db.String(30), db.ForeignKey('method.method_name'), nullable=False)


db.drop_all()

db.create_all()

db.session.query(OrmUser).delete()
db.session.query(OrmCountry).delete()
db.session.query(OrmClass).delete()
db.session.query(OrmMethod).delete()
db.session.query(OrmParameter).delete()


User1 = OrmUser(
    user_email='Sergei@gmail.com',
    user_name ='Sergei',
    user_age=20,
    user_university='KPI'
)

User2 = OrmUser(
    user_email='Igor@gmail.com',
    user_name ='Igor',
    user_age=25,
    user_university='NAU'
)
User3 = OrmUser(
    user_email='Petr@gmail.com',
    user_name ='Petr',
    user_age=16,
    user_university='KPI'
)
User4 = OrmUser(
    user_email='Gorg@gmail.com',
    user_name ='Georgiu',
    user_age=20,
    user_university='KNUBA'
)


Class1 = OrmClass(
    class_name='Numeric operations',
    methods_quantity=3,
    class_description='Class of basic actions with numbers',
    user_email='Gorg@gmail.com'
)

Class2 = OrmClass(
    class_name='Numeric operations advanced',
    methods_quantity=2,
    class_description='Complicated actions with numbers',
    user_email='Gorg@gmail.com'
)

Class3 = OrmClass(
    class_name='String operations',
    methods_quantity=2,
    class_description='Class of basic actions with strings',
    user_email='Petr@gmail.com'
)

Class4 = OrmClass(
    class_name='String operations advanced',
    methods_quantity=2,
    class_description='Complicated actions with strings',
    user_email='Sergei@gmail.com'
)

Method1 = OrmMethod(
    method_name='Adding numbers',
    method_description='Adding two numbers',
    output_type='Float',
    memory_size='32',
    class_name='Numeric operations'
)

Method2 = OrmMethod(
    method_name='Number exponentiation',
    method_description='Raising first number to the power of second one',
    output_type='Integer',
    memory_size='64',
    class_name='Numeric operations advanced'
)

Method3 = OrmMethod(
    method_name='Adding strings',
    method_description='Adding two strings',
    output_type='String',
    memory_size='128',
    class_name='String operations'
)

Method4 = OrmMethod(
    method_name='Finding string',
    method_description='Defies, if one string contains another',
    output_type='boolean',
    memory_size='256',
    class_name='String operations advanced'
)

Parameter1 = OrmParameter(
    parameter_name='Parameter 1',
    parameter_type='integer',
    parameter_description='First parameter',
    method_name='Finding string'
)

Country1 = OrmCountry(
    country_name ='Country1',
    founding_year=1225,
    president='pres1',
    government_struct='unitary',
    user_email='Sergei@gmail.com'

)

Country2 = OrmCountry(
    country_name ='Country2',
    founding_year=1225,
    president='pres2',
    government_struct='democratic',
    user_email='Petr@gmail.com'

)

Country3 = OrmCountry(
    country_name ='Country3',
    founding_year=1225,
    president='pres3',
    government_struct='democratic',
    user_email='Gora@gmail.com'
)

Country4 = OrmCountry(
    country_name ='Country4',
    founding_year=1225,
    president='pres4',
    government_struct='unitary',
    user_email='Igor@gmail.com'
)
db.session.add_all([
    User1,
    User2,
    User3,
    User4,
    Class1,
    Class2,
    Class3,
    Class4,
    Method1,
    Method2,
    Method3,
    Method4,
    Parameter1])

db.session.commit()

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/users')
def users():
    res = db.session.query(OrmUser).all()

    return render_template('users_table.html', users=res)



@app.route('/create_user', methods=['POST', 'GET'])
def create_user():
    form = UserForm()


    if request.method == 'POST':
        if form.validate():
            try:
                new_user = OrmParameter(
                    user_email=form.user_email.data,
                    user_name=form.user_name.data,
                    user_age=form.user_age.data,
                    user_university=form.user_university.data
                )
                db.session.add(new_user)
                db.session.commit()
                return render_template('success.html')
            except:
                return render_template('user_form.html', form=form)
        else:
            return render_template('user_form.html', form=form)
    elif request.method == 'GET':
        return render_template('user_form.html', form=form)


@app.route('/user_edit/<string:user_email>', methods=['GET', 'POST'])
def edit_user(user_email):
    form = EditUserForm()
    result = db.session.query(OrmUser).filter(OrmUser.user_email == user_email).one()

    if request.method == 'GET':

        form.user_name.data = result.user_name
        form.user_age.data = result.user_age
        form.user_university.data = result.user_university

        return render_template('edit_user.html', form=form, form_name='edit user')
    elif request.method == 'POST':
        if form.validate():
            try:
                result.user_name = form.user_name.data
                result.user_age = form.user_age.data
                result.user_university = form.user_university.data

                db.session.commit()
                return redirect('/users')
            except:
                return render_template('edit_user.html', form=form)
        else:
            return render_template('edit_user.html', form=form)


@app.route('/delete_user/<string:user_email>', methods=['GET', 'POST'])
def delete_user(user_email):
    result = db.session.query(OrmUser).filter(OrmUser.user_email == user_email).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')





@app.route('/country')
def country():
    res = db.session.query(OrmCountry).all()

    return render_template('country_table.html', countrys=res)


@app.route('/new_country', methods=['POST', 'GET'])
def new_country():
    form = CountryForm()


    if request.method == 'POST':
        if form.validate():
            try:
                new_country = OrmCountry(
                    country_name=form.country_name.data,
                    founding_year=form.founding_year.data,
                    president=form.president.data,
                    government_struct=form.government_struct.data
                )
                db.session.add(new_country)
                db.session.commit()
                return render_template('success.html')
            except:
                return render_template('country_form.html', form=form)
        else:
            return render_template('country_form.html', form=form)
    elif request.method == 'GET':
        return render_template('country_form.html', form=form)


@app.route('/edit_country/<string:country_name>', methods=['GET', 'POST'])
def edit_country(country_name):
    form = EditCountryForm()
    result = db.session.query(OrmCountry).filter(OrmCountry.country_name == country_name).one()

    if request.method == 'GET':

        form.founding_year.data = result.founding_year
        form.president.data = result.president
        form.government_struct.data = result.government_struct

        return render_template('edit_country.html', form=form, form_name='edit country')
    elif request.method == 'POST':
        if form.validate():
            try:
                result.founding_year = form.founding_year.data
                result.president = form.president.data
                result.government_struct = form.government_struct.data

                db.session.commit()
                return redirect('/country')
            except:
                return render_template('edit_country.html', form=form)
        else:
            return render_template('edit_country.html', form=form)


@app.route('/delete_country/<string:country_name>', methods=['GET', 'POST'])
def delete_country(country_name):
    result = db.session.query(OrmCountry).filter(OrmCountry.country_name == country_name).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')


@app.route('/class')
def classes():
    res = db.session.query(OrmClass).all()

    return render_template('class_table.html', classes=res)

@app.route('/new_class/<string:user_email>', methods=['GET', 'POST'])
def new_class(user_email):
    form = ClassForm()

    u_id_prep = db.session.query(OrmUser.user_email).filter(OrmUser.user_email == user_email).one()
    u_id = u_id_prep[0]

    if request.method == 'POST':
        if form.validate():
            try:
                new_class = OrmClass(
                    class_name=form.class_name.data,
                    methods_quantity=form.methods_quantity.data,
                    class_description=form.class_description.data,
                    user_email=u_id
                )
                db.session.add(new_class)
                db.session.commit()
                return render_template('success.html')
            except:
                return render_template('class_form.html', form=form)
        else:
            return render_template('class_form.html', form=form)
    elif request.method == 'GET':
        return render_template('class_form.html', form=form)

@app.route('/edit_class/<string:class_name>', methods=['GET', 'POST'])
def edit_class(class_name):
    form = EditClassForm()
    result = db.session.query(OrmClass).filter(OrmClass.class_name == class_name).one()

    if request.method == 'GET':

        form.methods_quantity.data = result.methods_quantity
        form.class_description.data = result.class_description

        return render_template('edit_class.html', form=form, form_name='edit class')
    elif request.method == 'POST':

        if form.validate():
            try:
                result.methods_quantity = form.methods_quantity.data
                result.class_description = form.class_description.data

                db.session.commit()
                return redirect('/class')
            except:
                return render_template('edit_class.html', form=form)
        else:
            return render_template('edit_class.html', form=form)



@app.route('/delete_feature/<string:class_name>', methods=['GET', 'POST'])
def delete_class(class_name):
    result = db.session.query(OrmClass).filter(OrmClass.class_name == class_name).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')


@app.route('/class')
def classes():
    res = db.session.query(OrmClass).all()

    return render_template('class_table.html', classes=res)

@app.route('/new_class/<string:user_email>', methods=['GET', 'POST'])
def new_class(user_email):
    form = ClassForm()

    u_id_prep = db.session.query(OrmUser.user_email).filter(OrmUser.user_email == user_email).one()
    u_id = u_id_prep[0]

    if request.method == 'POST':
        if form.validate():
            try:
                new_class = OrmClass(
                    class_name=form.class_name.data,
                    methods_quantity=form.methods_quantity.data,
                    class_description=form.class_description.data,
                    user_email=u_id
                )
                db.session.add(new_class)
                db.session.commit()
                return render_template('success.html')
            except:
                return render_template('class_form.html', form=form)
        else:
            return render_template('class_form.html', form=form)
    elif request.method == 'GET':
        return render_template('class_form.html', form=form)

@app.route('/edit_class/<string:class_name>', methods=['GET', 'POST'])
def edit_class(class_name):
    form = EditClassForm()
    result = db.session.query(OrmClass).filter(OrmClass.class_name == class_name).one()

    if request.method == 'GET':

        form.methods_quantity.data = result.methods_quantity
        form.class_description.data = result.class_description

        return render_template('edit_class.html', form=form, form_name='edit class')
    elif request.method == 'POST':

        if form.validate():
            try:
                result.methods_quantity = form.methods_quantity.data
                result.class_description = form.class_description.data

                db.session.commit()
                return redirect('/class')
            except:
                return render_template('edit_class.html', form=form)
        else:
            return render_template('edit_class.html', form=form)



@app.route('/delete_feature/<string:class_name>', methods=['GET', 'POST'])
def delete_class(class_name):
    result = db.session.query(OrmClass).filter(OrmClass.class_name == class_name).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')



# remedy
@app.route('/methods')
def methods():
    res = db.session.query(OrmMethod).all()

    return render_template('methods_table.html', methods=res)


@app.route('/new_method/<string:class_name>', methods=['GET', 'POST'])
def new_method(class_name):
    form = MethodForm()

    f_id_prep = db.session.query(OrmClass.class_name).filter(OrmClass.class_name == class_name).one()
    f_id = f_id_prep[0]

    if request.method == 'POST':
        if form.validate():
            try:
                new_method = OrmMethod(
                    method_name=form.method_name.data,
                    method_description=form.method_description.data,
                    output_type=form.output_type.data,
                    class_name=f_id
                )
                db.session.add(new_method)
                db.session.commit()
                return render_template('success.html')
            except:
                return render_template('method_form.html', form=form)
        else:
            return render_template('method_form.html', form=form)
    elif request.method == 'GET':
        return render_template('method_form.html', form=form)


@app.route('/edit_method/<string:method_name>', methods=['GET', 'POST'])
def edit_method(method_name):
    form = EditMethodForm()
    result = db.session.query(OrmMethod).filter(OrmMethod.method_name == method_name).one()

    if request.method == 'GET':

        form.founding_year.data = result.method_description
        form.output_type.data = result.output_type

        return render_template('edit_method.html', form=form, form_name='edit method')
    elif request.method == 'POST':
        if form.validate():
            try:
                result.method_description = form.method_description.data
                result.output_type = form.output_type.data
                db.session.commit()
                return redirect('/methods')
            except:
                return render_template('edit_method.html', form=form)
        else:
            return render_template('edit_method.html', form=form)


@app.route('/delete_method/<string:method_name>', methods=['GET', 'POST'])
def delete_method(method_name):
    result = db.session.query(OrmMethod).filter(OrmMethod.method_name == method_name).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')



@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    my_query = (
        db.session.query(
            OrmUser.user_email,
            func.count(OrmClass.class_name).label('classes_count')
        ).join(OrmClass, OrmClass.user_email == OrmUser.user_email).
            group_by(OrmUser.user_email)
    ).all()

    re_query = (
        db.session.query(
            OrmClass.class_name,
            func.count(OrmMethod.method_name).label('methods_count')
        ).join(OrmMethod, OrmMethod.class_name == OrmClass.class_name).
            group_by(OrmClass.class_name)
    ).all()


    user_id, feature_count = zip(*my_query)

    bar = go.Bar(
        x=user_id,
        y=feature_count
    )

    feature_id, remedy_count = zip(*re_query)
    pie = go.Pie(
        labels=feature_id,
        values=remedy_count
    )

    data = {
        "bar": [bar],
        "pie": [pie],

    }
    graphs_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html', graphsJSON=graphs_json)

if __name__ == '__main__':
    app.debug = True
    app.run()
