#!/usr/bin/env python3
"""
9-element_length module
Provides a type-annotated function that returns the length
of elements in an iterable.
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples with each element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing
        sequence-like elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        an element from the iterable and its length.
    """
    return [(i, len(i)) for i in lst]
