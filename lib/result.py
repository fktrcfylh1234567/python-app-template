from dataclasses import dataclass
from typing import Any, Optional, TypeAlias


@dataclass
class Ok:
    value: Any


@dataclass
class Err:
    e: Optional[Any] = None


Result: TypeAlias = Ok | Err

# example
if __name__ == '__main__':
    def foo() -> Result:
        return Ok("")


    match foo():
        case Ok(it):
            print("ok", it)
        case Err(e):
            print("error", e)
