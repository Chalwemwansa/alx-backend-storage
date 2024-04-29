#!/usr/bin/env python3
""" script finds the given schools where they offer
a given topic or course"""


def schools_by_topic(mongo_collection, topic):
    """the actual function that checks if the course
    is offered at the school"""
    obj_list = mongo_collection.find({"topics": {"$in": [topic]}})
    return obj_list
