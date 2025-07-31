#!/usr/bin/env python3
"""
6-sum_mixed_list module
Provides a type-annotated function to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
