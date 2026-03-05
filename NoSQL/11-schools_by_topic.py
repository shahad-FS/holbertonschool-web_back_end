#!/usr/bin/env python3
""" function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """return list of docs"""
    documents = mongo_collection.find({"topics": topic})
    list_docs = [i for i in documents]
    return list_docs
