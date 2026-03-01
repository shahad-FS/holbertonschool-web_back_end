#!/usr/bin/env python3
"""
function named index_range that takes 
two integer arguments page and page_size.
"""


def index_range(page, page_size):
    """
     return a tuple of size two containing a start index and an end index
     corresponding to the range of indexes
     return in a list for those particular pagination parameters.
     """
     start_at = (page - 1) * page_size
     end_at = start_at + page_size
     return (start_at, end_at)

