import asyncio

import aiohttp
from lib.result import *


async def request_async(method: str, url: str, **kwargs) -> Result:
    # default is 5 min, which is too long
    if 'timeout' not in kwargs.keys():
        kwargs['timeout'] = 1

    async with aiohttp.ClientSession() as session:
        try:
            async with session.request(method, url, **kwargs) as resp:
                if not resp.ok:
                    return Err(resp.status)

                return Ok(await resp.json())
        except BaseException as e:
            return Err(e)


if __name__ == '__main__':
    async def main():
        res = await request_async('post', 'https://httpbin.org/post', json={'key': 'value'})
        match res:
            case Ok(it):
                print("ok:", it)
            case Err(e):
                print("error:", e)


    asyncio.run(main())
