#!/usr/bin/env python3
"""
Handles pagination with resilience against deletions.
"""

import csv
import math
from typing import List, Dict


class Server:
    """Handles pagination of the baby names dataset."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary with paginated data, resilient to deletions."""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        dataset_size = len(indexed_data)
        assert index < dataset_size

        data = []
        next_index = index
        for _ in range(page_size):
            while (next_index < dataset_size and
                    indexed_data.get(next_index) is None):
                next_index += 1
            if next_index < dataset_size:
                data.append(indexed_data[next_index])
            next_index += 1

        return {
            "index": index,
            "next_index": next_index if next_index < dataset_size else None,
            "page_size": page_size,
            "data": data,
        }
