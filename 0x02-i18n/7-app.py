#!/usr/bin/env python3
"""
Basic Flask app with Babel for i18n, locale parameter, and mock login.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _, format_datetime
import pytz
from pytz.exceptions import UnknownTimeZoneError


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Config class for setting available languages and other settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


def get_user() -> dict:
    """
    Get the user dictionary by ID.
    Returns:
        The user dictionary if found, None otherwise.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    Function to be executed before each request.
    Sets the user in flask.g.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages or use the locale
    parameter if present.
    Returns:
        The best match for the user's preferred language or the specified locale.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the best time zone.
    Returns:
        The best time zone or UTC if none is found or invalid.
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            return pytz.timezone(g.user['timezone']).zone
        except UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> str:
    """
    Route for the index page.
    Returns:
        The rendered HTML for the index page.
    """
    current_time = format_datetime()
    return render_template('7-index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(debug=True)
