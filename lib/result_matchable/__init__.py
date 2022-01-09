from dataclasses import dataclass
from typing import Any, Optional, TypeAlias, Callable


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


def run_catching(f, *args, **kwargs) -> Result:
    try:
        return Ok(f(*args, **kwargs))
    except BaseException as e:
        return Err(e)


# decorator
def resultify(block) -> Callable[..., Result]:
    def f(*args, **kwargs):
        return run_catching(block, *args, **kwargs)

    return f
