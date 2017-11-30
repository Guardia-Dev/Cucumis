from functools import wraps
from flask import jsonify, current_app, request
from flask_apscheduler import APScheduler

from . import main
from app.spider.dbhelper import cache_query as query
from app.spider.dbhelper import cache_update as update


def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function


@main.route('/api/v1/test')
def api_test():
    return 'test'


@main.route('/api/v1/rss', methods=['GET'])
def api_rss_list():
    return api_rss_list_query()


@main.route('/api/v1/rss_update', methods=['GET'])
@support_jsonp
def api_rss_list_update():
    update()
    return jsonify({
        'code': 200,
        'items': query(),
        'message': 'rss parse success!',
    })


@main.route('/api/v1/rss_query', methods=['GET'])
def api_rss_list_query():
    return jsonify({
        'code': 200,
        'items': query(),
        'message': 'rss query success!',
    })

