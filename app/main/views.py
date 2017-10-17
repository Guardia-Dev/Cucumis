from . import main
from flask import render_template

import app.spider.rss as rss_tools

@main.route('/')
def hello():
    # posts = []
    posts = rss_tools.get_post_list()
    return render_template('rss.html', posts = posts)



# @main.route('/index/')
# @login_required
# def index():
#     return 'HelloWorld'
