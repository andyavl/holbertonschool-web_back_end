#!/usr/bin/env python3
"""A Python function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have the given topic in their
    'topics' field.

    Args:
        mongo_collection: a pymongo Collection object
        topic (str): the topic to search for

    Returns:
        List of matching documents (empty list if none)
    """
    return list(mongo_collection.find({"topics": topic}))
