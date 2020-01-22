from flask import abort, flash, redirect, render_template, url_for
from app import app

from functools import wraps
from .models import SubjectForm, LabForm, LabResultForm, StudentForm, SkillForm, StudentSkillForm
from . import session
from . import ReflectedModels, db
from .graphs import create_plot
import sqlalchemy

def table_view(fn):
    @wraps(fn)
    def view(*args, **kwargs):
        table_name = kwargs['table_name']
        if not table_name:
            return abort(404)
        if table_name not in ReflectedModels:
            return abort(404)
        table_instances = session.query(ReflectedModels[table_name])
        table_fields = ReflectedModels[table_name].__table__.columns.keys()
        if "%s_id" % table_name in table_fields:
            table_instances = table_instances.order_by("%s_id" % table_name).all()
        else:
            table_instances = table_instances.all()
        # return render_template('%s/%ss.html' % (table_name, table_name),
        #                        title="%ss" % table_name, **{'%ss' % table_name: instances})
        return render_template('table_instances.html', table_name=table_name,
                               table_instances=table_instances, table_fields=table_fields)
    return view

@app.route('/table/<table_name>', methods=['GET', 'POST'])
@table_view
# @login_required
def list_tables(table_name):
    """
       List all table instances
    """
    return table_name

def add_table_instance_decorator(fn):
    @wraps(fn)
    def view(*args, **kwargs):
        table_name = kwargs['table_name']
        if not table_name:
            return abort(404)
        if table_name not in ReflectedModels:
            return abort(404)
        # check_admin()
        add_instance = True
        form = globals()["".join([i[0].upper() + i[1:] for i in table_name.split("_")]) + "Form"]()
        table_fields = ReflectedModels[table_name].__table__.columns.keys()
        if form.validate_on_submit():
            max_id = session.query(ReflectedModels[table_name]).order_by(getattr(ReflectedModels[table_name], table_name + '_id').desc()).first()
            fields = {i: form[i].data for i in table_fields if i != (table_name + '_id')}
            fields[table_name + '_id'] = getattr(max_id, table_name + '_id') + 1
            try:
                table_instance = ReflectedModels[table_name](**fields)
                # add department to the database
                session.add(table_instance)
                session.commit()
                flash('You have successfully added a new table_instance.')
            except Exception as e:
                # in case department name already exists
                print(e)
                session.rollback()
                flash("Error: Can't create instance (check existence of instances with selected id or correctness of other fields)")

            # redirect to departments page
            return redirect(url_for('list_tables', table_name=table_name))

        # load department template
        return render_template('table_instance.html', action="Add",
                               add_instance=add_instance, form=form,
                               table_name=table_name)
    return view

@app.route('/table/<table_name>/add', methods=['GET', 'POST'])
@add_table_instance_decorator
# @login_required
def add_table_instance(table_name):
    """
    Add a table_instance to the database
    """
    return table_name

def edit_table_instance_decorator(fn):
    @wraps(fn)
    def view(*args, **kwargs):
        table_name = kwargs['table_name']
        instance_id = kwargs['id']
        if not table_name or not instance_id:
            return abort(404)
        if table_name not in ReflectedModels:
            return abort(404)
        # check_admin()
        add_instance = False
        try:
            table_fields = ReflectedModels[table_name].__table__.columns.keys()
            table_instance = session.query(ReflectedModels[table_name]).filter_by(**{table_name+'_id': instance_id}).first()
            if not table_instance:
                abort(404)
            form = globals()["".join([i[0].upper() + i[1:] for i in table_name.split("_")]) + "Form"]
            form = form(obj=table_instance)
        except:
            abort(404)
        if form.validate_on_submit():
            try:
                for table_field in table_fields:
                    if table_field != (table_name + '_id'):
                        setattr(table_instance, table_field, form[table_field].data)
                session.commit()
                flash('You have successfully edited the table_instance.')
            except Exception as e:
                # in case department name already exists
                print(e)
                session.rollback()
                flash("Error: Can't edit instance (check existence of instances with selected id or correctness of other fields)")
            # redirect to the departments page
            return redirect(url_for('list_tables', table_name=table_name))

        for table_field in table_fields:
            if table_field != (table_name + '_id'):
                setattr(form, table_field, getattr(table_instance, table_field))

        return render_template('table_instance.html', action="Edit",
                               add_instance=add_instance, form=form,
                               table_name=table_name)
    return view

@app.route('/table/<table_name>/edit/<int:id>', methods=['GET', 'POST'])
@edit_table_instance_decorator
# @login_required
def edit_table_instance(table_name, id):
    """
    Edit a table_instance to the database
    """
    return table_name

def delete_table_instance_decorator(fn):
    @wraps(fn)
    def view(*args, **kwargs):
        table_name = kwargs['table_name']
        instance_id = kwargs['id']
        if not table_name or not instance_id:
            return abort(404)
        if table_name not in ReflectedModels:
            return abort(404)
        # check_admin()
        add_instance = False
        table_fields = ReflectedModels[table_name].__table__.columns.keys()
        table_instance = session.query(ReflectedModels[table_name]).filter_by(**{table_name+'_id': instance_id}).first()
        if not table_instance:
            abort(404)
        session.delete(table_instance)
        session.commit()
        flash('You have successfully deleted the table_instance.')
        return redirect(url_for('list_tables', table_name=table_name))
    return view

@app.route('/table/<table_name>/delete/<int:id>', methods=['GET', 'POST'])
@delete_table_instance_decorator
# @login_required
def delete_table_instance(table_name, id):
    """
    Delete a table_instance to the database
    """
    return table_name

@app.route('/')
@app.route('/index')
def home_page():
    sql_cmd_graph1 = sqlalchemy.text('''   select student.student_name, count(lab_result.lab_id) 
                                    from student, lab_result 
                                    where student.student_id = lab_result.student_id 
                                    group by student.student_name''')
    results_graph1 = session.execute(sql_cmd_graph1).fetchall()
    sql_cmd_graph2 = sqlalchemy.text('''   select subject.subject_name, count(lab.lab_id) 
                                    from lab, subject 
                                    where lab.subject_id = subject.subject_id 
                                    group by subject.subject_name''')
    results_graph2 = session.execute(sql_cmd_graph2).fetchall()
    graphsPie, graphsBar = create_plot(results_graph1, results_graph2)
    return render_template('index.html', plot1=graphsPie, plot2=graphsBar)