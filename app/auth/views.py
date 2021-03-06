import sqlalchemy.exc
from flask import render_template, url_for, session, flash
from flask_login import login_required, logout_user, login_user
from werkzeug.utils import redirect
from app.auth import auth
from flask import request as req


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    username = req.args.get("username")
    email = req.args.get("email_address")
    password = req.args.get("password")

    try:
        if username is not None and email is not None and password is not None:
            from app.models import User
            from datetime import datetime

            now = datetime.now()
            user = User(email=email, username=username, password=password, profile_pic_path="no_path",
                        timestamp=now.strftime("%m/%d/%Y, %H:%M:%S"), last_login="")
            from app import db
            db.session.add(user)
            db.session.commit()
            from app.email import mail_message
            mail_message("Welcome to Blog", "email/welcome_user", user.email, user=user)
            return redirect(url_for('auth.login'))
    except sqlalchemy.exc.IntegrityError and RuntimeError:
        return redirect(url_for('auth.login'))

    return render_template('forms/signup.html')


@auth.route('/login', methods=["GET"])
def login():
    email = req.args.get("email_address")
    password = req.args.get("password")
    if email is not None and password is not None:
        from app.models import User
        user = User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(password):
            login_user(user, True)
            from app import db
            from datetime import datetime
            now = datetime.now()

            user = User.query.filter_by(id=user.id).first()
            setattr(user, 'last_login', now.strftime("%m/%d/%Y, %H:%M:%S"))
            db.session.commit()
            return redirect(req.args.get('next') or url_for('main.index'))
        else:
            print("The login failed")
            redirect(url_for("auth.login"))

    return render_template('forms/login.html')


@auth.route('/logout')
@login_required
def logout():

    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for("main.index"))

