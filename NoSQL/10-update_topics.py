#!/usr/bin/env python3
"""
A Python function that changes all topics of a school document based
on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of all documents with the given school name.

    Args:
        mongo_collection: a pymongo Collection object
        name (str): the school name to update
        topics (list of str): list of topics to set

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
