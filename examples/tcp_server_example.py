import asyncio
import uuid

from lib.tcp_server import TcpServer, ClientSession

server = TcpServer()


@server.on_connected
async def on_connected_(session: ClientSession):
    print('on_connected', session.addr)
    session.data["user_id"] = uuid.uuid1()


@server.on_message
async def on_message(session: ClientSession, message: str):
    print(f"Received {message!r} from {session.data['user_id']}")
    await session.send(message)


@server.on_disconnected
async def on_disconnected(session: ClientSession):
    print('on_disconnected', session.data['user_id'])


if __name__ == '__main__':
    asyncio.run(server.run())
