#!/usr/bin/env python3
"""
Module for simple pagination of the Popular Baby Names dataset.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for a given page of data,
    helping us figure out which part of the dataset to fetch.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items to display per page.

    Returns:
        Tuple[int, int]: A tuple with the start index (inclusive)
        and the end index (exclusive) for slicing the list.
    """
    # Calculate the start and end index based on the page number and size
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class for handling the pagination of the popular baby names dataset."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Returns the cached dataset, loading it from the file if needed."""
        # If the dataset isn't already loaded, read it from the CSV file
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Fetches the data for the specified page, based on the given 
        page number and page size. If the page is out of bounds, returns an empty list.

        Args:
            page (int): The current page number (1-indexed). Must be > 0.
            page_size (int): The number of items per page. Must be > 0.

        Returns:
            List[List]: A list containing the rows for the requested page, or 
            an empty list if the page index is out of range.
        """
        # Validate the inputs for page and page_size
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        # Get the range of indices for this page
        start, end = index_range(page, page_size)
        dataset = self.dataset()

        # If the start index is out of bounds, return an empty list
        return dataset[start:end] if start < len(dataset) else []
