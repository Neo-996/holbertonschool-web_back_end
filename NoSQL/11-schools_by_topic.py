#!/usr/bin/env python3
"""Return the list of schools by topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Return the list by topic"""
    return mongo_collection.find({"topics": topic})
