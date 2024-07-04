#!/usr/bin/env python3
"""
type_annotated func
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns tuple
    """
    return (k, float(v ** 2))
