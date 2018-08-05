import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir,'data.db')
#engine = create_engine('mysql+pymysql://root:secreta123@localhost,data')
#SQLALCHEMY_DATABASE_URI = 'mysql://root:secreta123@localhost/data')
#SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'secreta123'
