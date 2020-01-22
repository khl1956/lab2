from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class SubjectForm(FlaskForm):
    """
    Form for admin to add or edit a subject
    """
    subject_name = StringField('subject_name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class StudentForm(FlaskForm):
    """
    Form for admin to add or edit a subject
    """
    student_name = StringField('student_name', validators=[DataRequired()])
    student_surname = StringField('student_surname', validators=[DataRequired()])
    student_course = IntegerField('student_course', validators=[DataRequired()])
    student_studybook = IntegerField('student_studybook', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LabForm(FlaskForm):
    """
    Form for admin to add or edit a subject
    """
    lab_number = IntegerField('lab_number', validators=[DataRequired()])
    subject_id = IntegerField('subject_id', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LabResultForm(FlaskForm):
    """
    Form for admin to add or edit a subject
    """
    lab_id = IntegerField('lab_id', validators=[DataRequired()])
    student_id = IntegerField('student_id', validators=[DataRequired()])
    is_passed = BooleanField('is_passed')
    submit = SubmitField('Submit')

class SkillForm(FlaskForm):
    """
    Form for admin to add or edit a subject
    """
    subject_id = IntegerField('subject_id', validators=[DataRequired()])
    skill_grade = StringField('skill_grade', validators=[DataRequired()])
    submit = SubmitField('Submit')

class StudentSkillForm(FlaskForm):
    """
    Form for admin to add or edit a subject
    """
    student_id = StringField('student_id', validators=[DataRequired()])
    skill_id = StringField('skill_id', validators=[DataRequired()])
    submit = SubmitField('Submit')