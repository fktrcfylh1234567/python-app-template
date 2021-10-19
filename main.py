import asyncio


async def foo():
    return 42


async def main():
    res = await foo()
    return res


if __name__ == '__main__':
    res = asyncio.run(main())
    print(res)
