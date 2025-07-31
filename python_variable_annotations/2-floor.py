#!/usr/bin/env python3
"""
2-floor module
Provides a type-annotated function to compute the floor of a float.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a floating-point number.

    Args:
        n (float): A floating-point number.

    Returns:
        int: The floor of n (largest integer <= n).
    """
    return math.floor(n)
