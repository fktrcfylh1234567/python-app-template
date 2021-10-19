import asyncio
from typing import Tuple, Callable, Awaitable

ClientAddress = Tuple[str, int]


class ClientSession:
    def __init__(self, addr: ClientAddress):
        self.addr = addr
        self.data = dict()


async def _empty_event(*args):
    return args


class TcpServer:
    on_connected_cb: Callable[[ClientSession], Awaitable] = _empty_event
    on_message_cb: Callable[[ClientSession, str], Awaitable] = _empty_event
    on_disconnected_cb: Callable[[ClientSession], Awaitable] = _empty_event

    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port

    async def run(self):
        server = await asyncio.start_server(self._handle_connection, self.host, self.port)

        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')

        async with server:
            await server.serve_forever()

    def on_connected(self, fn: Callable[[ClientSession], Awaitable]):
        self.on_connected_cb = fn
        return fn

    def on_message(self, fn: Callable[[ClientSession, str], Awaitable]):
        self.on_message_cb = fn
        return fn

    def on_disconnected(self, fn: Callable[[ClientSession], Awaitable]):
        self.on_disconnected_cb = fn
        return fn

    async def _handle_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        addr = writer.get_extra_info('peername')
        session = ClientSession(addr)
        await self.on_connected_cb(session)

        while True:
            data = await reader.read(100)
            if data == b'':
                break

            await self.on_message_cb(session, data.decode())

            writer.write(data)
            await writer.drain()

        writer.close()
        await self.on_disconnected_cb(session)
