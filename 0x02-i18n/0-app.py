#!/usr/bin/env python3
"""
Basic Flask app to display a welcome message.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """
    Route for the index page.
    Returns:
        The rendered HTML for the index page.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)
