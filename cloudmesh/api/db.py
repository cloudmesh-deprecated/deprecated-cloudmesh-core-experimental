"""
This module defines the database access layer to Cloudmesh
"""

import types

from traits.api import Any, Bool, HasTraits, Interface, List


class Entity(HasTraits):
    """
    Represents an object that has a presence in the database.
    """

    key = Any
    value = Any


class Query(object):
    """
    Build complex queries against a single table in the database
    """

    def __init__(self, table):
        self._table = table

    def and_(self, query):
        "Logical and with the given :class:`Query`"

    def or_(self, query):
        "Logical or with the given :class:`Query`"

    def limit(self, count):
        "Limit the results returned"


class Result(HasTraits):
    """
    Result of the operations on the Database
    """

    success = Bool
    _items = List(Entity)


    def one(self):
        "Retrive the first :class:`Entity`"
        return self._items[0]

    def __iter__(self):
        return iter(self._items)


class ICloudmeshDatabase(Interface):
    """
    Main entrypoint to interact with the database
    """

    def insert(self, value):
        """
        Insert a value into the database returning the :class:`Entity`
        """

    def update(self, entity):
        """
        Update a single entity in the database
        """

    def lookup(self, table, **kwargs):
        """
        Fetch a single :class:`Entity` from the database whose fields match **all** of *kwargs*
        """

    def query(self, query):
        """
        Evaluate the :class:`Query` and return the list of results
        """

    def delete(self, query):
        """
        Delete all the entries identified by evaluating the :class:`Query`
        """

    def remove(self, entity):
        """
        Delete the given :class:`Entity` from the database
        """
