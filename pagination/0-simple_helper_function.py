#!/usr/bin/env python3
"""Defines a function called index_range that accepts two integers:
page and page_size."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates and returns a tuple containing the start and end indices
    for slicing a list, based on the current page number and the number
    of items per page.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
