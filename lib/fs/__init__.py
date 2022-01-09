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
