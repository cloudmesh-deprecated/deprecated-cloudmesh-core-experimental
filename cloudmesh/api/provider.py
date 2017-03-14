from abc import ABCMeta, abstractmethod, abstractproperty


class Provider(object):
    __metaclass__ = ABCMeta

    ################################ properties

    @abstractproperty
    def name(self):
        "The name of this provider"

    @abstractproperty
    def nodes(self):
        """List the nodes running

        :returns: node information as key/value dict
        :rtype: :class:`list` of :class:`dict`
        """

    @abstractproperty
    def images(self):
        """List the images available

        :returns: information about each image
        :rtype: :class:`list` of :class:`dict`
        """

    @abstractproperty
    def flavors(self):
        """List the flavors available

        :returns: information about each flavor
        :rtype: :class:`list` of :class:`dict`
        """

    @abstractproperty
    def secgroups(self):
        """List the security groups available

        :returns: information about each security group
        :rtype: :class:`list` of :class:`dict`
        """

    @abstractproperty
    def addresses(self):
        """List the addresses available

        :returns: information about each address
        :rtype: :class:`list` of :class:`dict`
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

