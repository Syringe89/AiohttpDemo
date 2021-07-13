import jinja2
from aiohttp import web
import aiohttp_jinja2

from demo.routes import setup_routes


def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
    )
    setup_routes(app)
    return app
