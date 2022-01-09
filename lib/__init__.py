import time
from typing import Optional

from lib.result import resultify


def circuit_breaker(max_retries, fail_recover_sec):
    errors_count = 0
    last_fail_t: Optional[float] = None

    def decorator(block):
        def f(*args, **kwargs):
            nonlocal errors_count
            nonlocal last_fail_t

            if last_fail_t and errors_count > 0 and time.time() - last_fail_t > fail_recover_sec:
                errors_count = 0

            if errors_count >= max_retries:
                last_fail_t = time.time()
                raise Exception(f"Circuit Breaker is turned on for {block}")

            try:
                return block(*args, **kwargs)
            finally:
                errors_count += 1

        return f

    return decorator
