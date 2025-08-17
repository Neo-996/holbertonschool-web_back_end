#!/usr/bin/env python3
"""Contains functions and classes for paginating a dataset of popular baby names."""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function calculates the start and end indices for a given page of data.
    It helps us figure out which part of the dataset to retrieve based on the page number and size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple with the starting index (inclusive) and the ending index (exclusive).
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


class Server:
    """This class handles pagination for the popular baby names dataset."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset from the CSV file."""
        # If the dataset isn't already loaded, read it from the file
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Fetches a specific page of the dataset, based on the given page number and page size.

        Args:
            page (int): The current page number (1-indexed). Default is 1.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            List[List]: A list of rows corresponding to the requested page, or an empty list if the page is out of range.
        """
        # Ensure that both page and page_size are positive integers
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        # Use the index_range function to find the indices for the requested page
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # If the start index is past the end of the dataset, return an empty list
        if start_index >= len(dataset):
            return []

        # Return the portion of the dataset that corresponds to the current page
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Fetches a dictionary with pagination details for the dataset, including data for the requested page,
        and information about the previous and next pages.

        Args:
            page (int): The current page number (1-indexed). Default is 1.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            dict: A dictionary containing:
                - page_size: The number of items on the current page.
                - page: The current page number.
                - data: The rows on the current page.
                - next_page: The next page number, or None if it's the last page.
                - prev_page: The previous page number, or None if it's the first page.
                - total_pages: The total number of pages available.
        """
        # Get the total number of data entries in the dataset
        total_data = len(self.dataset())

        # Calculate the total number of pages
        total_pages = math.ceil(total_data / page_size)

        # Determine the next and previous page numbers, if applicable
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Get the data for the current page
        data = self.get_page(page, page_size)

        # Return a dictionary with the pagination info
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
