#!/usr/bin/env python3
"""Module for simple pagination of the Popular Baby Names dataset."""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return the start and end indexes for pagination."""
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate the baby names dataset."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the correct page of data."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
