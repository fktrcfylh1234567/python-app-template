from dataclasses import dataclass

from dataclasses_json import dataclass_json

from lib.http_client import request_async
from lib.io import run_blocking
from lib.result_matchable import Ok, Err


@dataclass_json
@dataclass
class MyClass:
    id: int
    name: str


async def main():
    print("hello io world")

    res = await request_async('get', 'https://httpbin.org/get')
    print(res)

    my_class = MyClass(1, "zuzuka")
    res = await request_async('post', 'https://httpbin.org/post', json=my_class)
    print(res)

    res = await request_async('post', 'https://httpbin.org/post', json=[my_class])
    print(res)

    res = await request_async('post', 'https://httpbin.org/post', json={'key': 'value'})
    match res:
        case Ok(it):
            print("ok:", it)
        case Err(e):
            print("error:", e)


if __name__ == '__main__':
    run_blocking(main)
