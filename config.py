from sqlalchemy import create_engine
from sqlalchemy import func

import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'data.db')

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:secreta123@127.0.0.1/data'

#engine = create_engine("mysql+mysqlconnector://root:secreta123@127.0.0.1/data",
            #                encoding='latin1', echo=True)

SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'secreta123'
