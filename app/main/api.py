from flask import jsonify

from . import main
import app.spider.rss as rss_tools


@main.route('/api/v1/test')
def api_test():
    return 'test'


@main.route('/api/v1/rss', methods=['GET'])
def api_rss_list():
    return api_rss_list_update()


@main.route('/api/v1/rss_update', methods=['GET'])
def api_rss_list_update():
    url_list = rss_tools.get_all_urls()
    return jsonify({
        'code': 200,
        'items': rss_tools.parser_2_post(url_list),
        'message': 'rss parse success!',
    })
