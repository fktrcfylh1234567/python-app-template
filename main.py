import asyncio

from lib.api import request_async


async def main():
    print("hello async world")

    res = await request_async('get', 'https://httpbin.org/get')
    print(res)


if __name__ == '__main__':
    asyncio.run(main())
