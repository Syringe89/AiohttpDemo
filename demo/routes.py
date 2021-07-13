from aiohttp.abc import Application
from .views import frontend


def setup_routes(app: Application):
    app.router.add_get('/', frontend.index)
