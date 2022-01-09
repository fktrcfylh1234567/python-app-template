from lib.result import *


@resultify
def foo_err_safe(param):
    print(param)
    raise RuntimeError("error")


@with_retry(max_retries=2, retry_delay_ms=500)
def foo_err_retry(param):
    print(param)
    raise RuntimeError("error")


if __name__ == '__main__':
    res, err = foo_err_safe(42)
    assert res is None
    assert err is not None

    foo_err_retry(42)
