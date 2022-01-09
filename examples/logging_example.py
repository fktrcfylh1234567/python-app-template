from lib.logging import *

setup_logging()


@logify
def foo(param):
    return param


def baz():
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
    baz()

    foo(42)
