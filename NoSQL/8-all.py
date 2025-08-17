#!/usr/bin/env python3
""" List all documents using Python """
import pymongo


def list_all(mongo_collection):
    """ List all documents in a collection """
    if mongo_collection is not None:
        document = mongo_collection.find()
        return list(document) if document else []
    return []
