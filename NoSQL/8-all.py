#!/usr/bin/env python3
"""A Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    Returns all documents in a collection.

    Args:
        mongo_collection: a pymongo Collection object

    Returns:
        List of documents (empty list if none)
    """
    if not mongo_collection:
        return []

    return list(mongo_collection.find())
