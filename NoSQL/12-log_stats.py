#!/usr/bin/env python3
"""A Python script that provides some stats about Nginx logs stored in MongoD"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
