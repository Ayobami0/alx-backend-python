#!/usr/bin/python3
"""9. Let's duck type an iterable object."""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Checks the length of elements in an iterable

    Param:
        lst (Iterable[Sequence]): the items
    Return:
        List[Tuple[Sequence, int]]: a list of tuple containing the item and its length.
    """
    return [(i, len(i)) for i in lst]
