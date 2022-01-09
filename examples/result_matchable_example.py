from lib.result_matchable import *


def foo() -> Result:
    return Ok("data")


def baz() -> Result:
    return Err()


def foo_ok():
    return 42


def foo_err():
    raise RuntimeError("error")


@resultify
def foo_err_safe(param):
    print(param)
    raise RuntimeError("error")


if __name__ == '__main__':
    match foo():
        case Ok(it):
            print("ok:", it)
        case Err(e):
            print("error:", e)

    assert foo().unwrap() == "data"
    assert baz().or_else("null").unwrap() == "null"

    res = run_catching(foo_ok)
    assert res == Ok(value=42)

    foo_err = resultify(foo_err)
    res = foo_err()
    assert type(res) is Err

    res = foo_err_safe(42)
    assert type(res) is Err
