from typing import Callable

from lib.result import *
from lib.result import Ok, Err


def resultify(block) -> Callable[[], Result]:
    def f():
        try:
            return Ok(block())
        except BaseException as e:
            return Err(e)

    return f


# example
if __name__ == '__main__':
    def foo_ok():
        return 42


    def foo_err():
        raise RuntimeError("error")


    foo_ok_safe = resultify(foo_ok)
    match foo_ok_safe():
        case Ok(it):
            print("ok", it)
        case Err(e):
            print("error", e)

    foo_err_safe = resultify(foo_err)
    match foo_err_safe():
        case Ok(it):
            print("ok", it)
        case Err(e):
            print("error", e)
