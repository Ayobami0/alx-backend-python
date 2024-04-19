#!/usr/bin/env python3
"""11. More involved type annotations"""

from collections.abc import Mapping
from types import NoneType
from typing import Any, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, NoneType] = None
) -> Union[T, NoneType]:
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
