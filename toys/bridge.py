from collections import namedtuple
from functools import partial, wraps
from itertools import product
import types


class IResource(object):

    data = None

    def allocate(self):
        raise NotImplementedError

    def deallocate(self):
        raise NotImplementedError


class _Bridge(IResource):
    def __init__(self):
        self.__implementation = None


class NodeResource(_Bridge):

    def __init__(self, implementation):
        self.__implementation = implementation

    def allocate(self):
        self.data = self.__implementation.allocate()

    def deallocate(self):
        self.__implementation.deallocate()


class IPResource(_Bridge):
    def __init__(self, implementation):
        self.__implementation = implementation

    def allocate(self):
        self.data = self.__implementation.allocate()

    def deallocate(self):
        self.data = None
        self.__implementation.deallocate()


class NoOpResource(IResource):
    def allocate(self):
        pass

    def deallocate(self):
        pass


class ImplementationInterface:
    def allocate(self):
        raise NotImplementedError

    def deallocate(self):
        raise NotImplementedError


class Ec2Node(ImplementationInterface):
    def allocate(self):
        print "allocate node: ec2"
        return dict(provider='ec2')

    def deallocate(self):
        print 'deallocate node: ec2'


class Ec2IP(ImplementationInterface):
    def allocate(self):
        print 'allocate ip: ec2'
        return 'ec2:0.0.0.0'

    def deallocate(self):
        print 'deallocate ip: ec2'


class AzureNode(ImplementationInterface):
    def allocate(self):
        print 'allocate node: azure'
        return dict(provider='azure')

    def deallocate(self):
        print 'deallocate node: azure'


class AzureIP(ImplementationInterface):
    def allocate(self):
        print 'allocate ip: azure'
        return 'azure:0.0.0.0'

    def deallocate(self):
        print 'deallocate ip: azure'


class Composite(object):

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


entry = namedtuple('MappingEntry', ['node', 'ip'])
bridge_mapping = dict(
    ec2 = entry(Ec2Node, Ec2IP),
    azure = entry(AzureNode, AzureIP),
)


class NodeFacade(IResource):

    def __init__(self, name, provider='ec2', ip=False):

        self.name = name

        NodeImpl, IPImpl = bridge_mapping[provider]

        self._node = NodeResource(NodeImpl())

        if ip:
            self._ip = IPResource(IPImpl())
        else:
            self._ip = NoOpResource()

        self._resources = Composite([self._node, self._ip])

    @property
    def public_ip(self):
        if self._ip.data:
            return self._ip.data

    @property
    def provider(self):
        return self._node.data['provider']

    def allocate(self):
        self._resources.allocate()

    def deallocate(self):
        self._resources.deallocate()



def main():
    nodes = [
        NodeFacade('a'),
        NodeFacade('b', ip=True),
        NodeFacade('c', provider='azure'),
        NodeFacade('d', provider='azure', ip=True),
    ]

    cluster = Composite(nodes)
    cluster.allocate()

    for node in cluster.elements:
        print node.name, 'provider', node.provider
        print node.name, 'address', node._ip.data

    cluster.deallocate()


if __name__ == "__main__":
    main()
