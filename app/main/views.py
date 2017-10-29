from . import main
from flask import render_template

from app.spider.dbhelper import cache_query as query

@main.route('/')
def hello():
    # posts = []
    posts = query()
    return render_template('rss.html', posts = posts)



# @main.route('/index/')
# @login_required
# def index():
#     return 'HelloWorld'
