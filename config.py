

""" This is main config file for flask microblog
    application
"""

class Config(object):
    import os
    BaseDir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'string'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BaseDir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    import configparser

    set = configparser.ConfigParser()
    set.read(os.path.join(BaseDir,'CONFIGURATION.ini'))
    MAIL_SERVER = os.environ.get('MAIL') or set['MAIL']['SERVER']
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or set['MAIL']['PORT'])
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or set['MAIL']['TLS']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or set['MAIL']['USERNAME']
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or set['MAIL']['PASSWORD']
    ADMINS = ['applicationhanderrb@gmail.com']

