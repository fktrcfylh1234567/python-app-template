import asyncio
from asyncio import coroutine
from typing import Tuple, Callable

ClientAddress = Tuple[str, int]


class ClientSession:
    def __init__(self, addr: ClientAddress):
        self.addr = addr
        self.data = dict()


class TcpServer:
    on_connected: Callable[[ClientSession], coroutine]
    on_message: Callable[[ClientSession, str], coroutine]
    on_disconnected: Callable[[ClientSession], coroutine]

    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port

    async def run(self):
        server = await asyncio.start_server(self._handle_connection, self.host, self.port)

        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')

        async with server:
            await server.serve_forever()

    async def _handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        addr = writer.get_extra_info('peername')
        session = ClientSession(addr)
        await self.on_connected(session)

        while True:
            data = await reader.read(100)
            if data == b'':
                break

            await self.on_message(session, data.decode())

            writer.write(data)
            await writer.drain()

        print("Close the connection")
        writer.close()
        await self.on_disconnected(session)
