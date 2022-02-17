from asyncio import run_coroutine_threadsafe
from django.shortcuts import render

from flask import render_template, url_for, flash, redirect, request, Blueprint
from lava.users.forms import RegistatonForm, LoginForm

users = Blueprint('users', __name__)



@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistatonForm()
    if form.validate_on_submit():
        flash(f'Your account has been created. You can login now!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html',title='Register',form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
