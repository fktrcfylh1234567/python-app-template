import asyncio


def run_blocking(f, *args, **kwargs):
    try:
        return asyncio.run(f(*args, **kwargs)), None
    except BaseException as e:
        return None, e
