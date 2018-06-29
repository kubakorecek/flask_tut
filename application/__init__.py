"""This is main init file.
"""
import logging
import os
from logging.handlers import SMTPHandler,RotatingFileHandler


from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension


microapp = Flask(__name__)
microapp.config.from_object(Config)
db = SQLAlchemy(microapp)
migrate = Migrate(microapp, db)
login = LoginManager(microapp)
toolbar = DebugToolbarExtension(microapp)
login.login_view = 'login'


if not microapp.debug:

    if microapp.config['MAIL_SERVER']:
        auth = None
    if microapp.config['MAIL_USERNAME'] or microapp.config['MAIL_PASSWORD']:
        auth = (microapp.config['MAIL_USERNAME'], microapp.config['MAIL_PASSWORD'])
    secure = None
    if microapp.config['MAIL_USE_TLS']:
        secure = ()

    mail_handler = SMTPHandler(
        mailhost = (microapp.config['MAIL_SERVER'], microapp.config['MAIL_PORT']),
        fromaddr = 'no-reply@' + microapp.config['MAIL_SERVER'],
        toaddrs= ['applicationhanderrb@gmail.com'], subject='Microblog Failure',
        credentials=auth, secure=secure)
    mail_handler.setLevel(logging.ERROR)
    microapp.logger.addHandler(mail_handler)
if not microapp.debug:

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    microapp.logger.addHandler(file_handler)

    microapp.logger.setLevel(logging.INFO)
    microapp.logger.info('Microblog startup')

from application import routes
from application import models


