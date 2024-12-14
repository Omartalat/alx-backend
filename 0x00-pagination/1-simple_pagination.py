#!/usr/bin/env python3
"""This module provides functionality for paginating a dataset of
    popular baby names.

Functions:
    index_range(page: int, page_size: int) -> Tuple[int, int]:

Classes:
    Server:
        A class to paginate a database of popular baby names.

        Methods:
            __init__():
                Initializes the Server instance.

            dataset() -> List[List]:
                Returns the cached dataset of popular baby names.

            get_page(page: int = 1, page_size: int = 10) -> List[List]:"""

import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


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
        Retrieves a page of data from the dataset.
        Args:
            page (int): The page number to retrieve. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.
        Returns:
            List[List]: A list of lists containing the data for
                        the specified page. If the start index is greater
                        than or equal to the length of the dataset,
                        an empty list is returned.
        Raises:
            AssertionError: If `page` or `page_size` is not a positive integer.
        """

        assert type(page) is int and page > 0 and type(
            page_size) is int and page_size > 0
        dataset = self.dataset()
        index_tuple: Tuple = index_range(page, page_size)
        start: int = index_tuple[0]
        end: int = index_tuple[1]
        pages: List = dataset[start:end]

        dataset_length = len(self.__dataset)
        if start >= dataset_length:
            return []
        return pages
