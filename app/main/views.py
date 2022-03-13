from flask import render_template, url_for, session
from flask import request as req
from werkzeug.utils import redirect
from flask_login import current_user
from app.main import main


@main.route('/')
def index():
    """Render the index template"""
    username = None
    try:
        if current_user:
            username = current_user.username
    except AttributeError:
        print('An attr error occurred')

    return render_template('index.html', username=username)


@main.route('/blogs/create')
def new_blog():
    title = req.args.get("title")
    description = req.args.get("description")
    blog_txt = req.args.get("blog_txt")

    if title is not None and description is not None and blog_txt is not None:

        print(f'The blog\'s title is {title}, the description is {description} and the text is {blog_txt}')
        return redirect(url_for('main.index'))
    return render_template('forms/new_blog.html')


@main.route("/blogs/<int:blog_id>")
def view_blog(blog_id):

    return render_template('blog_view.html', blog_id=blog_id)


@main.route("/blogs/<int:blog_id>/comments")
def view_blog_comments(blog_id):
    return render_template('comments/comments_list.html', blog_id=blog_id)

