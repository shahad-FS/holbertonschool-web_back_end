#!/usr/bin/env python3
"""
function that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """"
    name (string) will be the school name to update
    topics (list of strings) will be the list of topics
    approached in the school
    """
    query = {"name": name}
    new_value = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_value)
