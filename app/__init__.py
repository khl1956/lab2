from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)
Base = declarative_base()

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
metadata = MetaData(bind=engine)
Base.metadata = metadata
ReflectedModels = dict()
metadata.reflect()
for tablename, tableobj in metadata.tables.items():
    ReflectedModels[tablename] = type(str(tablename), (Base,), {'__table__' : tableobj })
    print("Reflecting {0}".format(tablename))
Session = sessionmaker(bind=engine)
session = Session()

from app import routes, models