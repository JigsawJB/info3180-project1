import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://zidnvhnqzaoksf:c56fea815819d9360f019fe338e2442f632de61f70007918fce0e8343fc026f8@ec2-3-225-213-67.compute-1.amazonaws.com:5432/d7mcbanutoueft', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_DATABASE_URI = 'postgresql://qqatgwupfjohnx:52b01ebeb15249c39331c3ef34f2fb06e99f2273e9512956652518131cd72432@ec2-54-157-79-121.compute-1.amazonaws.com:5432/dcl39530u49jin'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://zidnvhnqzaoksf:c56fea815819d9360f019fe338e2442f632de61f70007918fce0e8343fc026f8@ec2-3-225-213-67.compute-1.amazonaws.com:5432/d7mcbanutoueft'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = './uploads'
    
    