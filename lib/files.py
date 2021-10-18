import asyncio

import aiofiles


async def read_lines(filename: str):
    async with aiofiles.open(filename, mode='r') as f:
        async for line in f:
            yield line.replace("\n", "")


async def write_text(filename: str, data: str):
    async with aiofiles.open(filename, mode='w') as f:
        await f.write(data)


async def append_text(filename: str, data: str):
    async with aiofiles.open(filename, mode='a') as f:
        await f.write(data)


async def write_bytes(filename: str, data: bytes):
    async with aiofiles.open(filename, mode='wb+') as f:
        await f.write(data)


if __name__ == '__main__':
    async def main():
        async for line in read_lines("../requirements.txt"):
            print(line)

        await write_text("myfile", "zuzuka")
        await append_text("myfile", "zuzuka")
        await write_bytes("myfile", b"zuzuka")


    asyncio.run(main())
