import asyncio
from dataclasses import dataclass

from dataclasses_json import dataclass_json

from lib.api import request_async


@dataclass_json
@dataclass
class MyClass:
    id: int
    name: str


async def main():
    print("hello async world")

    res = await request_async('get', 'https://httpbin.org/get')
    print(res)

    my_class = MyClass(1, "zuzuka")
    res = await request_async('post', 'https://httpbin.org/post', json=my_class)
    print(res)

    res = await request_async('post', 'https://httpbin.org/post', json=[my_class])
    print(res)


def deco(fn):
    print(fn)
    return fn


@deco
async def foo():
    pass


if __name__ == '__main__':
    asyncio.run(main())
