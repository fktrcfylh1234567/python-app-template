from lib.result_matchable import *

if __name__ == '__main__':
    def foo() -> Result:
        return Ok("data")


    def baz() -> Result:
        return Err()


    match foo():
        case Ok(it):
            print("ok:", it)
        case Err(e):
            print("error:", e)

    print(foo().unwrap())
    print(baz().or_else("null").unwrap())


    def foo_ok():
        return 42


    def foo_err():
        raise RuntimeError("error")


    foo_ok_safe = resultify(foo_ok)
    print(foo_ok_safe())

    foo_err_safe = resultify(foo_err)
    print(foo_err_safe())
