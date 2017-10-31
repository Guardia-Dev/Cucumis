import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

basedir = os.path.abspath(os.path.dirname(__file__))

HEROKU_URI = 'postgres://iwcxypoullcotd:344b3734ff9c793c50bceeb5314efa108e80e4675c7081f53dab5f6c04907c5a@ec2-184-73-189-190.compute-1.amazonaws.com:5432/dfq6o8fr8mc2bb'
HEROKU_DEV_URI = 'postgresql://postgres:dhy94113@localhost:5432/postgres'

class config(object):

    # Secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Cucumis'

    # SQLALCHEMY Setting
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # APScheduler
    JOBS = [{
        'id': 'update-sqlcache',
        'func': 'app.spider.dbhelper:cache_update_with_context',
        'trigger': 'interval',
        'seconds': 60 * 30,
        'replace_existing': True,
    }]

    SCHEDULER_API_ENABLED = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or HEROKU_DEV_URI
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(SQLALCHEMY_DATABASE_URI)
    }


class TestingConfig(config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'test')
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(SQLALCHEMY_DATABASE_URI)
    }


class ProductionConfig(config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or HEROKU_URI
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(SQLALCHEMY_DATABASE_URI)
    }


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': ProductionConfig,
}
