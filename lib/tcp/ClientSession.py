import asyncio

from lib.tcp import ClientAddress


class ClientSession:
    def __init__(self, addr: ClientAddress, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self.addr = addr
        self.data = dict()

        self._reader = reader
        self._writer = writer

    async def send(self, msg: str):
        self._writer.write(msg.encode())
        await self._writer.drain()
