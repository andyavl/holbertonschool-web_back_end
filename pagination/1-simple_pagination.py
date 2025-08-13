#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple

"""
index_range module

Provides a utility function to calculate the start and end indices
for paginating a list of items.
"""


def index_range(page, page_size) -> Tuple:
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data from the dataset.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start, end = index_range(page, page_size)

        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
