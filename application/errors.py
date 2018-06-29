from flask import render_template
from application import microapp
from application import db

@microapp.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@microapp.errorhandler(404)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500





