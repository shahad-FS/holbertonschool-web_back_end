#!/usr/bin/env python3
""" Write a Python script that provides some stats about
    Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    """ Database: logs
        Collection: nginx
    """
    client = MongoClient()
    col = client.logs.nginx

    count = col.count_documents({})
    get = col.count_documents({"method": "GET"})
    post = col.count_documents({"method": "POST"})
    put = col.count_documents({"method": "PUT"})
    patch = col.count_documents({"method": "PATCH"})
    delete = col.count_documents({"method": "DELETE"})
    status = col.count_documents({"method": "GET", "path": "/status"})

    print(f"{count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status} status check")
