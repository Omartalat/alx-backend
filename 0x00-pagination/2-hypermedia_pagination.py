#!/usr/bin/env python3
"""
pagination information.
"""

import csv
import math
from typing import Tuple, List, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """
        Returns a dictionary containing pagination information.
        Args:
            page (int): The current page number. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.
        Returns:
            Dict[str, any]: A dictionary containing the following keys:
                - page_size (int): The number of items per page.
                - page (int): The current page number.
                - data (List[List]): The data for the current page.
                - next_page (Optional[int]): The next page number, or None if
                  there is no next page.
                - prev_page (Optional[int]): The previous page number,
                  or None if there is no previous page.
                - total_pages (int): The total number of pages.
        """

        dataset = self.dataset()
        data: List[List] = self.get_page(page, page_size)
        next_page: int = page + 1
        previous_page: int = page - 1
        total_pages: int = math.ceil(len(dataset) / page_size)
        if next_page > total_pages:
            next_page = None
        if previous_page <= 0:
            previous_page = None
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': previous_page,
            'total_pages': total_pages
        }
