#!/usr/bin/env python3
""" this python script retuns all the attributes contained in a given mongo
    db document"""


def list_all(mongo_collection):
    """the function that returns the list of attributes
        of the document in list format"""
    if mongo_collection.count_documents({}) == 0:
        return []
    return mongo_collection.find()
