import logging

_log_format = f"%(asctime)s - [%(levelname)s] - %(filename)s %(funcName)s(line %(lineno)d) - %(message)s"
logging.basicConfig(level=logging.INFO, format=_log_format)


def foo():
    try:
        raise Exception(':nut:')
    except BaseException as e:
        logging.exception("", exc_info=e)


if __name__ == '__main__':
    # add filemode="w" to overwrite
    # logging.basicConfig(filename="sample.log", level=logging.INFO)

    logging.debug("This is a debug message")
    logging.info("Informational message")
    logging.error("An error has happened!")
    foo()
