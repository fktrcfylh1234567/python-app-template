import asyncio

import aiohttp
from lib.result import *


async def request_async(method: str, url: str, **kwargs) -> Result:
    # default is 5 min, which is too long
    if 'timeout' not in kwargs.keys():
        kwargs['timeout'] = 1

    json_ = kwargs.get('json')

    # dataclass
    if json_ and type(json_) not in [dict, list, set]:
        kwargs['json'] = json_.to_dict()

    # list of dataclass
    if json_ and type(json_) in [list, set] and len(json_) > 0 and json_[0] is not dict:
        kwargs['json'] = [it.to_dict() for it in json_]

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
