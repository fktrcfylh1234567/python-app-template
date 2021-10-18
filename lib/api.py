import asyncio

import aiohttp
from lib.result import *


async def request_async(method: str, url: str, **kwargs) -> Result:
    if 'timeout' not in kwargs.keys():
        kwargs['timeout'] = 1

    async with aiohttp.ClientSession() as session:
        try:
            async with session.request(method, url, **kwargs) as resp:
                if not resp.ok:
                    return Err(resp.status)

                return await resp.json()
        except BaseException as e:
            return Err(e)


if __name__ == '__main__':
    async def main():
        res = await request_async('post', 'https://httpbin.org/post', json={'key': 'value'})
        print(res)


    asyncio.run(main())
