from dataclasses import dataclass
from typing import Any, Optional, TypeAlias


@dataclass
class Ok:
    value: Any

    def unwrap(self):
        return self.value


@dataclass
class Err:
    e: Optional[Any] = None

    def unwrap(self):
        raise RuntimeError(f"trying to unwrap {self}!")


Result: TypeAlias = Ok | Err

# example
if __name__ == '__main__':
    def foo() -> Result:
        return Ok("data")


    match foo():
        case Ok(it):
            print("ok:", it)
        case Err(e):
            print("error:", e)

    print(foo().unwrap())
