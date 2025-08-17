#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient

def get_db_collection():
    """Connect to the MongoDB database and return the 'nginx' collection."""
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx
    return collection

def get_total_logs(collection):
    """Return the total number of documents in the collection."""
    return collection.count_documents({})

def get_method_counts(collection, methods):
    """
    Return a dictionary where the keys are methods and the values are the number
    of documents in the collection that have the corresponding method.
    """
    return {method: collection.count_documents({'method': method}) for method in methods}

def get_status_count(collection):
    """
    Return the number of documents in the collection where the method is 'GET'
    and the path is '/status'.
    """
    return collection.count_documents({'method': 'GET', 'path': '/status'})

def print_stats(total_logs, method_counts, status_count):
    """Print the stats."""
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_count} status check")

def main():
    """Main function to run the script."""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    collection = get_db_collection()
    total_logs = get_total_logs(collection)
    method_counts = get_method_counts(collection, methods)
    status_count = get_status_count(collection)
    print_stats(total_logs, method_counts, status_count)


# """Log stats"""
# from pymongo import MongoClient



# client = MongoClient('mongodb://localhost:27017/')


# db = client.logs
# collection = db.nginx

# total_logs = collection.count_documents({})

# methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
# method_counts = {method: collection.count_documents({'method': method}) for method in methods}

# status_count = collection.count_documents({'method': 'GET', 'path': '/status'})

# print(f"{total_logs} logs")
# print("Methods:")
# for method, count in method_counts.items():
#     print(f"\tmethod {method}: {count}")
# print(f"{status_count} status check")
if __name__ == "__main__":
    main()
