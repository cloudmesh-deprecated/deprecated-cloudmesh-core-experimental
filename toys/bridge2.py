from abc import ABCMeta, abstractmethod, abstractproperty
from functools import partial


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


class IResource(object):
    __metaclass__ = ABCMeta

    data = None

    @abstractmethod
    def allocate(self):
        pass

    @abstractmethod
    def deallocate(self):
        pass


class Bridge(object):

    def __init__(self, implementation):
        self._implementation = implementation



class ResourceBridge(IResource, Bridge):

    def allocate(self):
        return self._implementation.allocate()

    def deallocate(self):
        return self._implementation.deallocate()




class KeyApi(IResource):
    __metaclass__ = ABCMeta

    @abstractproperty
    def fingerprint(self):
        "Fingerprint of the key"

    @abstractproperty
    def kind(self):
        "Kind of the key: ssh, password, etc"


class IpApi(IResource):
    __metaclass__ = ABCMeta

    @abstractproperty
    def address(self):
        "The ip address"


class SecgroupApi(IResource):
    __metaclass__ = ABCMeta

    @abstractproperty
    def protocol(self):
        "icmp, tcp"

    @abstractproperty
    def ingress_ports(self):
        "List of port numbers allowed in. 'None' = all, '[]' = none"

    @abstractproperty
    def egress_ports(self):
        "list of port numbers allowed out. 'None' = all, '[]' = none"


class ImageApi(IResource):
    __metaclass__ = ABCMeta

    @abstractproperty
    def image_name(self):
        "Name of the image"

    @abstractproperty
    def os_name(self):
        "Operating system name: ubuntu, centos, rhel, suse, arch, etc"

    @abstractproperty
    def arch(self):
        "Architecture: amd64, x86, etc"


class NodeApi(IResource):
    __metaclass__ = ABCMeta

    def __init__(self, **config):
        self.config = config

    @abstractproperty
    def ident(self):
        "Provider identifier"

    @abstractproperty
    def addresses(self):
        "List of IP address resources belonging to this node"

    @abstractproperty
    def keys(self):
        "List of Key resources belonging to this node"

    @abstractproperty
    def usernames(self):
        "List login username resources that can be used to log into this node"


class OpenStackImage(ImageApi):

    @property
    def arch(self):
        raise NotImplementedError()

    @property
    def os_name(self):
        raise NotImplementedError()

    @property
    def image_name(self):
        raise NotImplementedError()

    def allocate(self):
        print 'allocate/image/ec2'

    def deallocate(self):
        print 'deallocate/image/ec2'


class OpenStackIP(IpApi):

    @property
    def address(self):
        return 'ec2:0.0.0.0'

    def allocate(self):
        print 'allocate/ip/ec2', self.address

    def deallocate(self):
        print 'deallocate/ip/ec2', self.address


class OpenStackNode(NodeApi):

    def __init__(self, *args, **kwargs):
        super(OpenStackNode, self).__init__(*args, **kwargs)

        self._image = OpenStackImage()
        self._addresses = [OpenStackIP()]

        self._resources = Composite([self._image] + self._addresses)

    @property
    def addresses(self):
        raise NotImplementedError()

    @property
    def ident(self):
        raise NotImplementedError()

    @property
    def keys(self):
        raise NotImplementedError()

    @property
    def usernames(self):
        raise NotImplementedError()

    def allocate(self):
        self._resources.allocate()
        print 'allocate/node/ec2'

    def deallocate(self):
        print 'deallocate/node/ec2'
        self._resources.deallocate()


cluster = Composite([OpenStackNode(),
                     OpenStackNode(),
                     OpenStackNode(),
                     ])
cluster.allocate()
cluster.deallocate()
