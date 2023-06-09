import os
from decouple import config


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config:
    SECRET_KEY = config('SECRET_KEY', 'secret')

class DevConfig(Config):
    DEBUG = config("FLASK_DEBUG")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(BASE_DIR, "db.sqlite3")


class TestConfig(Config):
    pass
class ProdConfig(Config):
    pass



config_dict ={
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}