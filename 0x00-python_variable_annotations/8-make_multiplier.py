#!/usr/bin/env python3
"""
type_annotated func
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
     takes a float multiplier as argument and returns
     a function that multiplies a float by multiplier
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func
