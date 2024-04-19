#!/usr/bin/python3
"""7. Complex types - string and int/float to tuple."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple from given arguments.

    Param:
        k (str): string
        v (int | float): interger or float
    Return:
        tuple[str | float]: a tuple containing both arguments
    """
    return (k, float(v**2))
