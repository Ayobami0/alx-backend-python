#!/usr/bin/env python3
"""12. Type Checking."""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms an array

    Return:
        List: the list of items
    """
    zoomed_in: List = [item for item in lst for _ in range(factor)]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
