from flask import render_template

from app.main import main


@main.route('/')
def index():
    """Render the index template"""

    return render_template('index.html', title="Th index")

