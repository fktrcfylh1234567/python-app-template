import time
from typing import Tuple, Optional, Any

Result = Tuple[Optional[Any], Optional[BaseException]]


def run_catching(f, *args, **kwargs) -> Result:
    try:
        return f(*args, **kwargs), None
    except BaseException as e:
        return None, e


def run_with_retries(f, *args, max_retries=100, retry_delay_ms=100, **kwargs) -> Result:
    err = None
    for i in range(max_retries):
        res, err = run_catching(f, *args, **kwargs)
        if err is None:
            return res, None

        time.sleep(retry_delay_ms / 1000)

    return None, err
