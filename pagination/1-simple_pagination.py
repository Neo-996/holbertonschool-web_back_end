#!/usr/bin/env python3
"""Defines the index_range function, the Server class, and the get_page method."""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple with the start and end indices for retrieving data 
    from a list, based on the page and page_size parameters.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset, loading it from the CSV if not cached."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the list of records for the requested page.
        Ensures the page and page_size are valid and fetches the data accordingly.
        """
        # Validate the page and page_size inputs
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        # Calculate the range of indexes to retrieve
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # If the start index exceeds the length of the dataset, return an empty list
        if start_index >= len(dataset):
            return []

        # Return the requested page of data
        return dataset[start_index:end_index]
