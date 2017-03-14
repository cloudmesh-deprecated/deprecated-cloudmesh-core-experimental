from abc import ABCMeta, abstractmethod, abstractproperty


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

