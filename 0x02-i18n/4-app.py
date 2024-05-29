#!/usr/bin/env python3
"""
Basic Flask app with Babel for i18n and locale parameter.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

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
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Route for the index page.
    Returns:
        The rendered HTML for the index page.
    """
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(debug=True)
