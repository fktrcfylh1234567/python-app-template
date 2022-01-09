import time
from typing import Tuple, Optional, Any, Callable

Result = Tuple[Optional[Any], Optional[BaseException]]
ResultifiedCallable = Callable[..., Result]


def run_catching(f, *args, **kwargs) -> Result:
    try:
        return f(*args, **kwargs), None
    except BaseException as e:
        return None, e


# decorator
def resultify(block) -> ResultifiedCallable:
    def f(*args, **kwargs):
        return run_catching(block, *args, **kwargs)

    return f


def run_with_retries(f, *args, max_retries=100, retry_delay_ms=100, **kwargs) -> Result:
    err = None
    for i in range(max_retries):
        res, err = run_catching(f, *args, **kwargs)
        if err is None:
            return res, None

        time.sleep(retry_delay_ms / 1000)

    return None, err


# decorator
def with_retry(max_retries=100, retry_delay_ms=100) -> Callable[[Callable], ResultifiedCallable]:
    def decorator(block) -> ResultifiedCallable:
        def f(*args, **kwargs):
            return run_with_retries(block, *args, max_retries=max_retries, retry_delay_ms=retry_delay_ms, **kwargs)

        return f

    return decorator
