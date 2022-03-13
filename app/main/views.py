from flask import render_template, url_for
from flask import request as req
from werkzeug.utils import redirect

from app.main import main


@main.route('/')
def index():
    """Render the index template"""

    return render_template('index.html', title="Th index")


@main.route('/blogs/create')
def new_blog():
    title = req.args.get("title")
    description = req.args.get("description")
    blog_txt = req.args.get("blog_txt")

    if title is not None and description is not None and blog_txt is not None:

        print(f'The blog\'s title is {title}, the description is {description} and the text is {blog_txt}')
        return redirect(url_for('main.index'))
    return render_template('forms/new_blog.html')

