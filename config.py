import os
import base64

basedir = os.path.abspath(os.path.dirname(__file__))

HEROKU_URI = 'postgres://iwcxypoullcotd:344b3734ff9c793c50bceeb5314efa108e80e4675c7081f53dab5f6c04907c5a@ec2-184-73-189-190.compute-1.amazonaws.com:5432/dfq6o8fr8mc2bb'

class config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Cucumis'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'postgresql://postgres:dhy94113@localhost:5432/postgres'

class TestingConfig(config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'test')

class ProductionConfig(config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or HEROKU_URI

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': ProductionConfig
}
