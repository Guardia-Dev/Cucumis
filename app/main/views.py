from . import main
from flask import request, render_template, redirect, url_for
from flask_login import login_required, login_user

@main.route('/')
def hello():
    return redirect(url_for('main.login'))

@main.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    nickname = request.form.get('nickname')
    password = request.form.get('password')
    if password == 'dhy94113':
        from app.models import User
        user = User.query.filter_by(nickname = nickname).first()
        if not user:
            return 'Bad login'
        login_user(user)
        return redirect(url_for('admin.index'))
    else:
        return 'Bad login'


# @main.route('/index/')
# @login_required
# def index():
#     return 'HelloWorld'
