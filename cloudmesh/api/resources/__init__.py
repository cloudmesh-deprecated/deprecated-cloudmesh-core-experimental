from abc import ABCMeta, abstractmethod, abstractproperty

from cloudmesh.util.patterns import Composite


class Resource(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def data(self):
        "A :class:`dict` representing the metadata about this resource"

    @abstractmethod
    def allocate(self):
        "Allocate this resource"

    @abstractmethod
    def deallocate(self):
        "Deallocate this resource"


class ResourceComposite(Resource):

    def __init__(self, elements):

        for elem in elements:
            assert isinstance(elem, Resource)

        self.composite = Composite(elements)

    @property
    def data(self):
        return None

    def getattr(self, name):
        "Return a list of attributes for each element"

        def gen():
            for elem in self.composite.elements:
                yield getattr(elem, name)

        return list(gen())

    def allocate(self):
        self.composite.allocate()

    def deallocate(self):
        self.composite.deallocate()
