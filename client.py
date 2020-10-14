import time

import aiohttp
import asyncio


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


loop = asyncio.get_event_loop()
start_time = time.time()
coroutines = [get("http://0.0.0.0:8080/check/1/2") for _ in range(1000)]

results = loop.run_until_complete(asyncio.gather(*coroutines))
end_time = time.time() - start_time
print(end_time)
