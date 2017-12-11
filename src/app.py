# import key pieces from bottle package
from bottle import route, run, static_file
# import os for reading environment variables
import os


def get_static_root():
    """
    Return root directory for static content
    """
    return os.environ.get('STATIC_CONTENT_ROOT', '/opt/app-root/src/static')


@route('/')
def root_page():
    """
    Route for root path, just try to return index.html
    """
    return static_file('/index.html', get_static_root())


@route('/static/<path:path>')
def server_static(path):
    """
    Any path not defined more specifically is handled as static content
    """
    return static_file(path, get_static_root())


@route('/healthz')
def healthz():
    """
    Status endpoint for health checks
    """
    return 'I can be iz healthy'


if __name__ == '__main__':
    # Here we simply start the server process
    run(host='0.0.0.0', port=8080, reloader=True)
