from flask import render_template, url_for
from flask import request as req
from werkzeug.utils import redirect
from flask_login import current_user
from app.main import main
from app.utils import format_default_timestamp_single


@main.route('/')
def index():
    """Render the index template"""
    username = None
    user_id = None
    try:
        if current_user:
            user_id = current_user.id
            username = current_user.username
    except AttributeError:
        print('An attr error occurred')

    from app.models import Blog
    blogs = Blog.query.all()

    return render_template('index.html', username=username, user_id=user_id, blogs_list=blogs)


@main.route('/blogs/create')
def new_blog():
    title = req.args.get("title")
    description = req.args.get("description")
    blog_txt = req.args.get("blog_txt")

    if title is not None and description is not None and blog_txt is not None:
        from app.models import Blog
        from datetime import datetime

        now = datetime.now()
        blog = Blog(blog_txt=blog_txt, creator_id=current_user.id, timestamp=now.strftime("%m/ %d/ %Y, %H:%M:%S"),
                    comments="", saves="", title=title, description=description)
        from app import db
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('forms/new_blog.html')


@main.route("/blogs/<int:blog_id>")
def view_blog(blog_id):

    return render_template('blog_view.html', blog_id=blog_id)


@main.route("/blogs/<int:blog_id>/comments")
def view_blog_comments(blog_id):
    return render_template('comments/comments_list.html', blog_id=blog_id)


@main.route('/users/<int:user_id>')
def view_profile(user_id):
    from app.models import User
    user = User.query.filter_by(id=user_id).first()
    if current_user.id == user.id:
        show_logout = True
    else:
        show_logout = False
    return render_template('profile/profile.html', user=user, timestamp=user.timestamp, logout=show_logout)

