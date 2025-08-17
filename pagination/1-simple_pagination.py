#!/usr/bin/env python3
"""Defines the index_range function, the Server class, and the get_page method."""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple with two values representing the start and end
    indices for fetching data from a list, based on the provided
    page number and page size.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


class Server:
    """Server class for handling pagination of a baby names database."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset, loading it from the CSV if necessary."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the data corresponding to the requested page from the dataset.
        It ensures valid input and calculates the right range of indices.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
