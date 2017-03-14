
"""
This module provides utilities for working with different design patterns
"""


from functools import partial


class Composite(object):

    """A ``Composite`` is a collection of objects.

    Our use-case this is interpreted as a collection of objects
    implementing the same interface.  This class allows dynamic
    invocation of a method upon all elements of the collection. This
    invocation does not return anything.

    """

    def __init__(self, elements):
        self.elements = elements

    def invoke(self, name, *args, **kwargs):
        for elem in self.elements:
            if not hasattr(elem, name):
                msg = 'Composite element {} has no method {}'.format(type(elem), name)
                raise AttributeError(msg)

        for elem in self.elements:
            fn = getattr(elem, name)
            fn(*args, **kwargs)

    def __getattr__(self, name):
        return partial(self.invoke, name)
