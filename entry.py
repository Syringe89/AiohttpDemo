from aiohttp import web
from demo import create_app
import asyncio

app = create_app()

if __name__ == '__main__':
    web.run_app(app)
