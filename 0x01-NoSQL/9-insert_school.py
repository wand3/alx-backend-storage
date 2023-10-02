#!/usr/bin/env python3
"""
This module have a utility function that insert documents and returns the new insertion _id
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert into school
    """
    return mongo_collection.insert_one(kwargs).inserted_id
