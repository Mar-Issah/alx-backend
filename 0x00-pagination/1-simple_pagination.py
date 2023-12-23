#!/usr/bin/env python3
"""1. Simple pagination"""
import csv
from typing import List, Tuple


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

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        Return a tuple of size two containing a start index and an end
        index corresponding to the range of indexes
        Args:
            page (int): the current page
            page_size (int): the size of the page

        Returns:
            (tuple): a tuple of the start and end index
        """
        nextPageIdx = page * page_size
        return nextPageIdx - page_size, nextPageIdx

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve items for the given page number
        Args:
            page (int): page number
            page_size (int): number of items on the page

        Returns:
            List(List): a list if inputs are within range or an empty list.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndex, endIndex = self.index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]
