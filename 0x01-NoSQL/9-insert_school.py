#!/usr/bin/env python3
""" script that inserts into a document in a given mongo db
    and returns the id of the object"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts the kwargs dictionary attributes into the mongo
    db database used in the calling script"""
    document = mongo_collection.insert_one(kwargs)
    document_id = document.inserted_id
    return document_id
