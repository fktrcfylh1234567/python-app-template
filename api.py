import aiohttp


async def request_async(method: str, url: str, **kwargs):
    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, **kwargs) as resp:
            return await resp.json()
