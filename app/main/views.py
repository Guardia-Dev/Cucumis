from . import main

@main.route('/')
def hello():
    return 'hello world'


# @main.route('/index/')
# @login_required
# def index():
#     return 'HelloWorld'
