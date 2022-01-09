import asyncio

from lib.fs import *


async def main():
    async for line in read_lines("../requirements.txt"):
        print(line)

    await write_text("myfile", "zuzuka")
    await append_text("myfile", "zuzuka")
    await write_bytes("myfile", b"zuzuka")


if __name__ == '__main__':
    asyncio.run(main())
