import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'jobberwocky'.encode('utf8')
