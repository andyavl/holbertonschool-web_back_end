#!/usr/bin/env python3
"""
7-to_kv module
Provides a type-annotated function that returns a tuple from
a string and a squared number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with a string and the square of a number.

    Args:
        k (str): A string key.
        v (Union[int, float]): A number to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is k and
                           the second is v squared (as a float).
    """
    return (k, float(v ** 2))
