from flask import render_template, url_for
from flask import request as req
from werkzeug.utils import redirect
from flask_login import current_user, login_required
from app.main import main
from app.requests import get_random_quote
from app.utils import format_blogs_array, format_comments_array


@main.route('/', methods=["GET"])
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
    formatted_blogs = format_blogs_array(blogs)
    quote = get_random_quote()
    return render_template('index.html', username=username, user_id=user_id, blogs_list=formatted_blogs, random_quote=quote)


@main.route('/blogs/create')
@login_required
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


@main.route("/blogs/<int:blog_id>", methods=["GET"])
def view_blog(blog_id):
    from app.models import Blog
    blog = Blog.query.filter_by(id=blog_id).first()
    try:
        if current_user.id == blog.creator_id:
            show_more_opts = True
        else:
            show_more_opts = False
    except AttributeError:
        show_more_opts = False
    return render_template('blog_view.html', blog=blog, show_more_opts=show_more_opts)


@main.route("/blogs/<int:blog_id>/comments", methods=["GET", "POST"])
def view_blog_comments(blog_id):
    comment_txt = req.args.get("comment")
    if comment_txt:
        try:
            if current_user is not None:
                if comment_txt is not None:
                    from app.models import Comment
                    from datetime import datetime

                    now = datetime.now()
                    comment = Comment(comment_txt=comment_txt, creator_id=current_user.id, blog_id=blog_id,
                                      timestamp=now.timestamp())
                    from app.models import Blog

                    from app import db
                    db.session.add(comment)
                    # pitch = Pitch.query().filter(Pitch.id == pitch_id).first()
                    blog = Blog.query.filter_by(id=blog_id).first()
                    setattr(blog, 'comments', Blog.comments + ",1")
                    db.session.commit()
        except AttributeError:
            print('An attr error occurred')



        # comments = Comment.query.filter_by(pitch_id=pitch_id)
        # comments_list = format_comments_array(comments)
        return redirect(url_for('main.view_blog_comments', blog_id=blog_id))
        # return render_template('comments/comments_list.html', title=f"Comments - {pitch_id}", comments_list=comments_list)
    else:
        from app.models import Comment
        from app.models import Blog
        blog = Blog.query.filter_by(id=blog_id).first()
        show_delete = None
        try:
            if blog and blog.creator_id == current_user.id:
                show_delete = True
        except AttributeError:
            print('An attr error occurred')

        comments = Comment.query.filter_by(blog_id=blog_id)
        comments_list = format_comments_array(comments)
        return render_template('comments/comments_list.html', title=f"Comments - {blog_id}", comments_list=comments_list, show_delete=show_delete)


@main.route('/users/<int:user_id>', methods=["GET"])
def view_profile(user_id):
    from app.models import User
    user = User.query.filter_by(id=user_id).first()
    from app.models import Blog
    blogs = Blog.query.filter_by(creator_id=user_id).all()
    formatted_blogs = format_blogs_array(blogs)
    try:
        if current_user.id == user.id:
            show_logout = True
        else:
            show_logout = False
    except AttributeError:
        show_logout = False

    return render_template('profile/profile.html', user=user, timestamp=user.timestamp, logout=show_logout,
                           blogs=formatted_blogs)


@main.route("/blogs/<blog_id>/delete")
@login_required
def delete_blog(blog_id):
    if blog_id:
        from app.models import Blog
        blog = Blog.query.filter_by(id=blog_id).first()
        if blog and blog.creator_id == current_user.id:
            from app import db
            db.session.delete(blog)
            db.session.commit()
    return redirect(url_for('main.index'))


@main.route("/blogs/<blog_id>/comments/<comment_id>/delete")
@login_required
def delete_comment(blog_id, comment_id):
    if blog_id:
        from app.models import Comment
        comment = Comment.query.filter_by(id=comment_id).first()
        if comment and comment.blog_id == blog_id:
            from app import db
            db.session.delete(comment)
            db.session.commit()
    return redirect(url_for('main.view_blog_comments', blog_id=blog_id))

