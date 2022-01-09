import logging


def setup_logging(level=logging.INFO, **kwargs):
    # _log_format = f"%(asctime)s - [%(levelname)s] - %(filename)s %(funcName)s (line %(lineno)d) - %(message)s"
    _log_format = f"%(asctime)s - [%(levelname)s] - %(filename)s (line %(lineno)d) - %(message)s"
    logging.basicConfig(level=level, format=_log_format, **kwargs)


def logify(block):
    def f(*args, **kwargs):
        logging.info(f"{block} called with params: {args} {kwargs}")
        res = block(*args, **kwargs)
        logging.info(f"{block} returned: {res}")
        return res

    return f
