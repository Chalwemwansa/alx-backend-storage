#!/usr/bin/env python3
"""script updates a given number of documents in a selected
collection based on the name of the document"""


def update_topics(mongo_collection, name, topics):
    """the function that checks for given documents with a particular
    name attribute then adds a topics list"""
    filter_dict = {"name": name}
    update_dict = {"$set": {"topics": topics}}
    mongo_collection.update_many(filter_dict, update_dict)
