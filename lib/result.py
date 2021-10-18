from dataclasses import dataclass
from typing import Any, Optional, TypeAlias


@dataclass
class Ok:
    value: Any

    def unwrap(self):
        return self.value

    def or_else(self, value):
        return self


@dataclass
class Err:
    e: Optional[Any] = None

    def unwrap(self):
        raise RuntimeError(f"trying to unwrap {self}!")

    @staticmethod
    def or_else(value):
        return Ok(value)


Result: TypeAlias = Ok | Err

# example
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
