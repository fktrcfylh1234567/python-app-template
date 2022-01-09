import logging
import time


def profile_time(block):
    def f(*args, **kwargs):
        t1 = time.time()
        res = block(*args, **kwargs)
        t2 = time.time()

        dt = (t2 - t1) * 1000
        dt = round(dt)
        logging.debug(f"{block} took {dt}ms to complete")
        return res

    return f
