from abc import ABCMeta, abstractmethod, abstractproperty

import logging
logger = logging.getLogger(__name__)


class Result(object):
    """The result of invoking a method on a :class:`Provider`.

    :class:`Result`\s have two properties:

      1. :meth:`id` (:class:`str`): the unambiguous provider identifier

      2. :meth:`attrs` (:class:`cloudmesh.util.Dot dict`): the
           properties of the result of whatever was invoked.

    A :class:`Result` has implemented several of the special method
    inherited from :class:`object`. This allows:


    >>> import pytest
    >>> r = Result('foo', dict(a=42, b=24, c='hello world'))
    >>> assert 'foo' == r, r.id
    >>> assert list(iter(r)) == list(iter(r.attrs))
    >>> assert r['a'] == r.attrs['a']
    >>> assert len(r) == len(r.attrs)
    >>> assert str(r) == 'foo'
    >>> assert r.a == r['a']
    >>> assert 'b' in r
    >>> assert r.items() == r.attrs.items()
    >>> assert r.values() == r.attrs.values()
    >>> assert r.keys() == r.attrs.keys()
    >>> with pytest.raises(TypeError):
    ...     Result(0xdeadbeef, {})
    >>> with pytest.raises(TypeError):
    ...     Result('ok', 0xdeadbeef)


    """

    __slots__ = ['_id', '_attrs']

    def __init__(self, ident, attrs):
        if not type(ident) == str:
            msg = '%s initialized incorrectly. `ident` should be `str` but got %s: %s' % \
                  (self.__class__.__name__, type(ident), ident)
            logger.warning(msg)
            raise TypeError(msg)

        if not isinstance(attrs, dict):
            msg = '%s initialized incorrectly. `attrs` should be a `dict` but got %s: %s' % \
                  (self.__class__.__name__, type(attrs), attrs)
            logger.warning(msg)
            raise TypeError(msg)

        self._id = ident
        self._attrs = attrs

    @property
    def id(self):
        return self._id

    @property
    def attrs(self):
        return self._attrs

    def __eq__(self, other):
        assert type(other) is str
        return other == self.id

    def __iter__(self):
        return iter(self._attrs)

    def __getitem__(self, key):
        return self._attrs[key]

    def __len__(self):
        return len(self._attrs)

    def __str__(self):
        return self.id

    def __getattr__(self, name):
        return self[name]

    def __contains__(self, item):
        return self.attrs.__contains__(item)

    def items(self):
        return self.attrs.items()

    def values(self):
        return self.attrs.values()

    def keys(self):
        return self.attrs.keys()



class Provider(object):
    __metaclass__ = ABCMeta

    ################################ properties

    @abstractproperty
    def name(self):
        "The name of this provider"

    ################################ listing

    @abstractmethod
    def nodes(self):
        """List the nodes running

        :returns: node information as key/value dict
        :rtype: :class:`list` of :class:`Result`
        """

    @abstractmethod
    def images(self):
        """List the images available

        :returns: information about each image
        :rtype: :class:`list` of :class:`Result`
        """

    @abstractmethod
    def flavors(self):
        """List the flavors available

        :returns: information about each flavor
        :rtype: :class:`list` of :class:`Result`
        """

    @abstractmethod
    def secgroups(self):
        """List the security groups available

        :returns: information about each security group
        :rtype: :class:`list` of :class:`Result`
        """

    @abstractmethod
    def addresses(self):
        """List the addresses available

        :returns: information about each address
        :rtype: :class:`list` of :class:`Result`
        """

    ################################ node methods

    @abstractmethod
    def allocate_node(self, **kwargs):
        """Allocate a node

        ``**kwargs`` are provider-specific properties of the node

        :returns: a provider-specific unambiguous node identifier
        """

    @abstractmethod
    def deallocate_node(self, ident):
        """De-allocate a node

        :param ident: the unambiguous provider identifier for the node to remove
        """

    @abstractmethod
    def get_node(self, ident):
        """Retrieve a node

        :param: ident: the unambiguous provider identifier
        """

    ################################ ip address methods

    def allocate_ip(self, **kwargs):
        """Allocate an ip address

        :returns: provider-specific identifier for the address"
        """

    def deallocate_ip(self, ident):
        """De-allocate an ip address

        :param str ident: provider-specific unambiguous identifier
        """

    def associate_ip(self, ip, node):
        """Associate ``ip`` with the given ``node``

        :param str ip: unambiguous provider identifier
        :param str node: unambiguous provider identifier
        """

    def disassociate_ip(self, ip, node):
        """Disassociate ``ip`` with the given ``node``

        :param str ip: unambiguous provider identifier
        :param str node: unambiguous provider identifier
        """

    @abstractmethod
    def get_ip(self, ident):
        """Retrieve a ip

        :param: ident: the unambiguous provider identifier
        """

    ################################ security group methods

    def allocate_secgroup(self, **kwargs):
        """Allocate a security group

        ``**kwargs`` are the provider-specific options

        :returns: a provider-specific unambiguous identifier for the security group
        """

    def deallocate_secgroup(self, ident):
        """Deallocate a security group

        :param str ident: unambiguous provider identifier
        """

    def modify_secgroup(self, ident, **kwargs):
        """Updated a preexisting security group

        This should not change the identifier

        :param str ident: unambiguous identifier
        """

    @abstractmethod
    def get_secgroup(self, ident):
        """Retrieve a secgroup

        :param: ident: the unambiguous provider identifier
        """

    ################################ key methods

    def allocate_key(self, **kwargs):
        """Allocate a key

        kwargs: provider-specific properties about the key

        :returns: unambiguous provider-specific identifier
        """

    def deallocate_key(self, ident):
        """Deallocate a key

        :param str ident: unambiguous provider-specific identifier
        """

    def modify_key(self, ident, **kwargs):
        """Modify a preexisting key

        This should not change the identifier.

        :param str ident: unambiguous provider-specific identifier
        :param kwargs: properties to update
        """

    @abstractmethod
    def get_key(self, ident):
        """Retrieve a key

        :param: ident: the unambiguous provider identifier
        """

    ################################ image methods

    def allocate_image(self, **kwargs):
        """Allocate an image

        :param kwargs: provider-specific properties
        :returns: unambiguous provider-specific identifier
        """

    def deallocate_image(self, ident):
        """Deallocate an image

        :param str ident: unambiguous provider-specific identifier
        """

    @abstractmethod
    def get_key(self, ident):
        """Retrieve a key

        :param: ident: the unambiguous provider identifier
        """

