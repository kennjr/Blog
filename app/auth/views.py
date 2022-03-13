from flask import render_template, url_for
from flask_login import login_required, logout_user, login_user
from werkzeug.utils import redirect


from app.auth import auth
from flask import request as req


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    username = req.args.get("username")
    email = req.args.get("email_address")
    password = req.args.get("password")

    if username is not None and email is not None and password is not None:
        from app.models import User
        user = User(email=email, username=username, password=password, profile_pic_path="no_path")
        from app import db
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('forms/signup.html')


@auth.route('/login', methods=["GET", "POST"])
def login():
    email = req.args.get("email_address")
    password = req.args.get("password")
    if email is not None and password is not None:
        from app.models import User
        user = User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(password):
            login_user(user, True)
            return redirect(req.args.get('next') or url_for('main.index'))
        else:
            print("The login failed")
            redirect(url_for("auth.login"))

    return render_template('forms/login.html')
