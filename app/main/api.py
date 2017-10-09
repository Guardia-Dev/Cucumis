from . import main

from flask import request, render_template, redirect, url_for, jsonify
from flask_login import login_required, login_user

@main.route('/api/v1/getPosts', methods = ['GET', 'POST'])
def getPosts():
    from app.models import Article
    posts = Article.query.all()
    res = []
    for post in posts:
        res.append(post.toDict())
    return jsonify({
        'code': 200,
        'result': res,
        'message': 'Get Guardia\'s posts',
    })

@main.route('/api/v1/getUsers', methods = ['GET', 'POST'])
def getUsers():
    from app.models import User
    users = User.query.all()
    res = []
    for user in users:
        res.append(user.toDict())
    return jsonify({
        'code': 200,
        'result': res,
        'message': 'Get all users',
    })
