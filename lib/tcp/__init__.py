from typing import Tuple

from lib.tcp.TcpServer import TcpServer
from lib.tcp.ClientSession import ClientSession

ClientAddress = Tuple[str, int]


async def _empty_event(*args):
    return args
