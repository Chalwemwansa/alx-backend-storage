#!/usr/bin/env python3
"""script gets t=some output from the logs in a given mongo db dump file
gets the number for each request and the total number of documents
in the dump"""
from pymongo import MongoClient


def print_log(mongo_collection):
    """the function that prints the results from the mongo collection passed"""
    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f"{mongo_collection.count_documents({})} logs")
    print("Methods:")
    for method in methods_list:
        print(f'\tmethod {method}: \
                {mongo_collection.count_documents({"method": method})}')
    filter = {"method": "GET", "path": "/status"}
    print(f'{mongo_collection.count_documents(filter)} status check')


if __name__ == "__main__":
    """execute the code only if its the script beng executed directly"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    print_log(log_collection)
