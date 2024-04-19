#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""

# The types of the elements of the input are not know
from types import NoneType
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """Gets the first item in a sequence

    Param:
        lst (Sequence[Any]): A squecnce of any object
    Return:
        Union[Any, None]: The first element in the
            sequence or None
    """
    if lst:
        return lst[0]
    else:
        return None
