#!/usr/bin/env python3
"""
A funtion that returns a tuple of size two containing start index and
end index corresponding to a portion of a list to display on a specific page.
"""


def index_range(page, page_size):

    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)
