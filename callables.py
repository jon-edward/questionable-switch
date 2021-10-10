from abc import ABC, abstractmethod
from textwrap import dedent
from typing import Union


class Callable(ABC):

    @abstractmethod
    def __call__(self):
        raise NotImplementedError


class CodeString(Callable):
    """Defines a string of code that is executed as a case.
    The variable name `value` in the code block is what's to be returned from it, by default."""

    def __init__(self, code: str, return_name: str = 'value', _globals: Union[dict, None] = None):
        self._code = code
        self._return_name = return_name
        self._globals = {} if _globals is None else _globals

    def __call__(self):
        code_elem = compile(dedent(self._code), "<string>", "exec")
        eval(code_elem, self._globals)
        return self._globals.get(self._return_name, None)


class CodeTuple(Callable):
    """Defines a tuple of statements, where the last element of the tuple is returned as the output."""

    def __init__(self, *args):
        self._tuple = args

    def __call__(self):
        if len(self._tuple) == 0:
            return None
        return self._tuple[-1]
