import asyncio

from lib.tcp_server import TcpServer, ClientSession


async def on_connected(session: ClientSession):
    print('on_connected', session.addr)
    session.data["user_id"] = "qwer"


async def on_message(session: ClientSession, message: str):
    print(f"Received {message!r} from {session.data['id']}")


async def on_disconnected(session: ClientSession):
    print('on_disconnected', session.data['id'])


async def main():
    server = TcpServer()

    server.on_connected = on_connected
    server.on_message = on_message
    server.on_disconnected = on_disconnected

    await server.run()


if __name__ == '__main__':
    asyncio.run(main())
