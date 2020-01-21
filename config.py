import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql+psycopg2://postgres:toor@127.0.0.1/lab_work_app'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    BOOTSTRAP_SERVE_LOCAL = True