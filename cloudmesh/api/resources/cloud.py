from abc import ABCMeta, abstractmethod, abstractproperty

from cloudmesh.api.resources import Resource as ResourceInterface


class CloudResource(ResourceInterface):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, **specification):
        "Define the resource using key/value pairs in **specification**"

    @abstractproperty
    def provider_id(self):
        "The identifier for this resource on the provider as a :class:`str`"


################################################################ Node

class Node(CloudResource):
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        "The name of this node"

    @abstractproperty
    def internal_ip(self):
        "The LAN IP address"

    @abstractproperty
    def external_ip(self):
        "The WAN IP address. ``None`` if not assigned"

    @abstractproperty
    def cores(self):
        "The number of cores available as :class:`int`"

    @abstractproperty
    def memory(self):
        "Amount of memory in MB as :class:`int`"

    @abstractproperty
    def disk(self):
        "Disk volume in GB as :class:`int`"

    @abstractproperty
    def loginuser(self):
        "Username to log into this node as :class:`str`"

    @abstractproperty
    def addresses(self):
        "All the Address Resources as :class:`list` of :class:`Address`"

    @abstractproperty
    def security_groups(self):
        "All security group resources as :class:`list` of :class:`Secgroup`"

    @abstractproperty
    def users(self):
        "All users availble as :class:`list` of :class:`User`"

    @abstractmethod
    def ssh(self, user=None, cmd=None):
        """Login and optionally run a command

        :param str user: Username to use. Default is the loginuser.
        :param str cmd: command to run. Default is an interactive login shell
        """


################################################################ User

class User(CloudResource):
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        "Name of this user as :class:`str`"

    @abstractproperty
    def keys(self):
        "SSH authorized keys as :class:`list` of :class:`Key`"

    @abstractmethod
    def add_key(self, key):
        """Add an authorized key

        :param Key key: a key to add
        """

    @abstractmethod
    def rm_key(self, key):
        """Remove an authorized key

        :param Key key: a key to remove
        """


################################################################ Key

class Key(CloudResource):
    __metaclass__ = ABCMeta

    @abstractproperty
    def fingerprint(self):
        "The key fingerprint"

    @abstractproperty
    def hash_method(self):
        "Fingerprint hashing algorithm (md5 or sha256)"

    @abstractproperty
    def pub(self):
        "The public key as :class:`str`"


################################################################ Secgroup

class Secgroup(CloudResource):
    __metaclass__ = ABCMeta

    @abstractproperty
    def protocols(self):
        """List of protocols defined by this secgroup.

        Protocols can be one of:

        - icmp
        - tcp
        - udp

        :rtype: :class:`list` of :class:`str`
        """

    @abstractproperty
    def ports(self):
        """List of ports on which the group is applied.

        :returns: :class:`list` of :class:`int`. A value of ``None``
        means "all ports" while an empty list means "no ports"
        """

    @abstractproperty
    def ingress(self):
        "The allowed ingress addresses as CIDR"

    @abstractproperty
    def egress(self):
        "The allowed egress addresses as CIDR"


################################################################ Address

class Address(CloudResource):
    __metaclass__ = ABCMeta

    def ip(self):
        "The default IP address"
        return self.ip4

    @abstractproperty
    def ip4(self):
        "The IPv4 address"


################################################################ Cluster

class Cluster(CloudResource):
    __metaclass__ = ABCMeta

    @abstractproperty
    def nodes(self):
        "A mapping from provider name to an implementing :class:`Node`"

    def nth(self, ix):
        return self.nodes.values()[ix]


################################################################ Image

class Image(CloudResource):
    __metaclass__ = ABCMeta

    @abstractproperty
    def os_flavor(self):
        "The flavor of the OS (eg 'ubuntu', 'centos', 'arch', 'nixos', etc)"

    @abstractproperty
    def version(self):
        "The version string of the image"

    @abstractproperty
    def arch(self):
        "The CPU architecture. One of 'x86', 'amd64'"

    @abstractproperty
    def loginuser(self):
        "Username of the admin login account as :class:`str`"
