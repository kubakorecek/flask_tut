"""Module operating running
"""
from application import microapp
from application import db

from application.models import User
from application.models import Post

@microapp.shell_context_processor
def make_shell_context():
    return {'db':db, 'User': User, 'Post':Post }





