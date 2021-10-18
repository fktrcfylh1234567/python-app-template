import asyncio

from api import request_async


async def main():
    print("hello async world")

    js = await request_async('get', 'https://httpbin.org/get')
    print(js)


if __name__ == '__main__':
    asyncio.run(main())
