from flask import render_template
from urllib import error


# @app.errorhandler(404)
from app.main import main


@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404_page.html'), 404


@main.app_errorhandler(error.HTTPError)
def http_error(error):
    return render_template('404_page.html'), 404
