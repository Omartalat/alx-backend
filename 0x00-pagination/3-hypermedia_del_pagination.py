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
        Retrieves a dictionary containing pagination information and data
        for a given index and page size.
        Args:
            index (int, optional): The starting index for pagination.
            Defaults to None. page_size (int, optional): The number
            of items per page. Defaults to 10.
        Returns:
            Dict[str, any]: A dictionary containing the following keys:
                - 'index': The current starting index.
                - 'next_index': The starting index for the next page, or
                    None if there are no more pages.
                - 'page_size': The number of items per page.
                - 'data': A dictionary of the data items for
                    the current page.
        """
        dataset = self.indexed_dataset()
        keys = sorted(dataset.keys())
        assert index is not None and index >= 0 and index < len(keys)
        next_index = index + page_size
        if next_index >= len(keys):
            next_index = None
        data = {}
        for key, val in dataset.items():
            if key in range(index, index + page_size):
                data[key] = val
        data_index = {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data,
        }
        return data_index