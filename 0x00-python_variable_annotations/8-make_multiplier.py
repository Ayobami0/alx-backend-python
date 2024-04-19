#!/usr/bin/env python3
"""8. Complex types - functions"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a fnction that mutiplies a float by supplied argument.

    Param:
        multipilier (float): float
    Return:
        Callable[[float], float]: a function that takes in a float
    """
    return lambda x: x * multiplier
