#!/usr/bin/env python3
"""
A Python function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a collection.

    Args:
        mongo_collection: a pymongo Collection object
        **kwargs: key-value pairs representing document fields

    Returns:
        The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
