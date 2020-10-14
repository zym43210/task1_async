import asyncio
import random

from aiohttp import web


async def handle(request):
    text = str(request.match_info.get('a') + request.match_info.get('b'))
    await asyncio.sleep(random.randint(0, 5))
    return web.Response(text=text)


app = web.Application()
app.router.add_get('/check/{a}/{b}', handle)

web.run_app(app)
