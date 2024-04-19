#!/usr/bin/env python3
"""11. More involved type annotations"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Safely gets a value.

    Param:
        dct (Mapping): a dictionary type
        key (Any): a key
        default (Union[TypeVar, None]): The defaulf value if
            key is non-existent
    Return:
        Union[Any, None]: the value or the default
    """
    if key in dct:
        return dct[key]
    else:
        return default
