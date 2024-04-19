#!/usr/bin/python3
"""5. Complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats and retuns the result

    Param:
        input_list (list[float]): list of float
    Return:
        float: the sum of the numbers in the list
    """
    return sum(input_list)
