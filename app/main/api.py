from functools import wraps
from flask import jsonify, current_app, request
from flask_apscheduler import APScheduler

from . import main
from app.spider.dbhelper import cache_query as query
from app.spider.dbhelper import cache_update as update

# jsonp support


def support_jsonp(f):
    @wraps(f)
    def dec_func(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + f(*args, **kwargs).data.decode('utf-8') + ')'
            return current_app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return dec_func


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

