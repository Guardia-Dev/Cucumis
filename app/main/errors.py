from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(error):
    return '404 error'

@main.app_errorhandler(500)
def internal_server_error(error):
    return '500 error'


