#!/usr/bin/env python3
"""Defines the index_range function, the Server class, and the get_page method."""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates and returns the start and end indices for a page
    of data. It helps us figure out which part of the list to fetch
    based on the current page and how many items per page we want.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


class Server:
    """A class to handle pagination for a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads the dataset, caching it for faster access on future calls."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Fetches the data for the specified page. It ensures that the
        page number and size are valid and returns the correct slice
        from the dataset.
        """
        # Make sure the page and page_size are positive integers
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        # Get the range of indices for this page
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # If the start index goes past the end of the dataset, return an empty list
        if start_index >= len(dataset):
            return []

        # Return the data for the current page
        return dataset[start_index:end_index]
