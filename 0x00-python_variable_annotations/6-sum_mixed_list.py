#!/usr/bin/env python3
"""6. Complex types - mixed list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of floats and/or ints and retuns the result

    Param:
        mxd_lst (list[float | int]): list of float or int
    Return:
        float: the sum of the numbers in the list
    """
    return sum(mxd_lst)
