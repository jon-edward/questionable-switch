from typing import Any, Hashable

from .callables import Callable
from .exceptions import CaseDoesNotExistError, UndefinedCasesError


_PREDEFINED_CASE = object()


class _Cases(dict):
    def __new__(cls, *args, **kwargs):
        return dict.__new__(_Cases, *args, **kwargs)

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            for k in key:
                dict.__setitem__(self, k, value)
        else:
            dict.__setitem__(self, key, value)


class Switch:
    """Used as a context manager to emulate common usages of a switch case statement.
    """

    def __init__(self, get_value: Hashable):
        self._cases = _Cases()
        self._get_value = get_value
        self._out_value = _PREDEFINED_CASE

    @property
    def value(self) -> Any:
        """Call `value` after defining cases for switch."""
        if self._out_value is _PREDEFINED_CASE:
            raise UndefinedCasesError("Cannot get switch result before cases are defined.")
        if isinstance(self._out_value, Callable):
            return self._out_value()
        return self._out_value

    def __enter__(self):
        return self._cases

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            out = self._cases[self._get_value]
        except KeyError:
            try:
                out = self._cases["default"]
            except KeyError:
                raise CaseDoesNotExistError(self._get_value)
        self._out_value = out
