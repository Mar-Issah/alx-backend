#!/usr/bin/env python3
"""0. Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index corresponding to the range of indexes
    Args:
        page (int): the current page
        page_size (int): the size of the page

    Returns:
        (tuple): a tuple of the start and end index
    """
    nextPageIdx = page * page_size
    return nextPageIdx- page_size, nextPageIdx
