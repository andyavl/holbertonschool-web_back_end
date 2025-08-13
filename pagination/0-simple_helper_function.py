#!/usr/bin/env python3
"""
index_range module

Provides a utility function to calculate the start and end indices
for paginating a list of items.
"""


def index_range(page, page_size):
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items to display per page.

    Returns:
        tuple: A tuple (start, end) representing the start index (inclusive)
               and the end index (exclusive) for slicing a list.

    Example:
        >>> index_range(1, 10)
        (0, 10)
        >>> index_range(3, 5)
        (10, 15)
    """
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)
