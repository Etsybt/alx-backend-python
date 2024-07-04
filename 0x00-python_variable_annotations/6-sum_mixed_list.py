#!/usr/bin/env python3
"""
sum of list of 2 types
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    type-annotated func, return sum as float for int, float list
    """
    return (sum(item for item in mxd_list if isinstance(item, (int, float))))
