#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with hypermedia pagination based on an index.
        """
        indexed_data = self.indexed_dataset()
        total_items = len(indexed_data)

        if index is not None:
            assert isinstance(index, int) and index >= 0
            if index >= total_items:

                return {
                    "index": index,
                    "data": [],
                    "page_size": 0,
                    "next_index": total_items
                }
        else:
            index = 0

        data = []
        current_index = index
        items_found = 0

        while items_found < page_size and current_index < total_items:

            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                items_found += 1
            current_index += 1

        next_index = current_index

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
