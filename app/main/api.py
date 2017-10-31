from flask import jsonify
from flask_apscheduler import APScheduler

from . import main
from app.spider.dbhelper import cache_query as query
from app.spider.dbhelper import cache_update as update

@main.route('/api/v1/test')
def api_test():
    return 'test'


@main.route('/api/v1/rss', methods=['GET'])
def api_rss_list():
    return api_rss_list_query()


@main.route('/api/v1/rss_update', methods=['GET'])
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

