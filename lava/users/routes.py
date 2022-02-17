from asyncio import run_coroutine_threadsafe
from django.shortcuts import render
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from lava.users.forms import RegistatonForm, LoginForm
from lava import db,bcrypt
from lava.models import User

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash(f'You are alread logged in!', 'success')
        return redirect(url_for('index'))
    form = RegistatonForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(name=form.name.data,
                    email=form.email.data, password=hashed_pass,gender=form.gender.data,date=form.b_date.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created. You can login now!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash(f'You are alread logged in!', 'success')
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # redirect ot next pager
            next_page = request.args.get('next')
            flash(f'You have successufily logged in!', 'success')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('index'))
        else:
            flash(f'Login unsuccessful, please email & password info', 'danger')
    return render_template('login.html', title='Login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    flash(f'You have successufily logged out!', 'success')
    return redirect(url_for('index'))
