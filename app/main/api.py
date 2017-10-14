from . import main

@main.route('/api/v1/test')
def api_test():
    return 'test'

