"""
This module provides the model API for components
"""

import copy

from sqlachemy import Table
from traits.api import DictStrAny, HasTraits, Interface, Str, UUID

from cloudmesh.core.util.db import traits2sql


class ISql(Interface):

    @classmethod
    def table(cls, metadata, mapper):
        "Return an SQLAlchemy Table"
        ts = copy.copy(cls.class_traits())
        ts.pop('trait_added', None)
        ts.pop('trait_modified', None)

        # mapping = traits2sql(mapper)
        # table = Table(cls.__class__.__name__, metadata,
                      

    def to_values(self):
        "Dict representation for submitting to the database"
        raise NotImplemented

    def from_values(self, dictionary):
        "Update attributes from database representation"
        raise NotImplemented


@provides(ISql)
class Node(HasTraits):

    provider_id = UUID          # id on the provider end (eg openstack, ec2, azure, etc)
    name = Str                  # name of the node
    # internal_ip = IPv4          # LAN network address
    # external_ip = IPv4          # WAN network address
    metadata = Trait(Dotdict)       # arbitrary metadata



class IResource(Interface):

    def allocate_node(self, node):
        "Start a node"

    def deallocate_node(self, node):
        "Remove a node and cleanup used resources"


class Cluster(HasTraits):
    "Cluster of nodes"

    pass


class ACL(HasTraits):
    "Access Control Groups"

    pass


class Key(HasTraits):
    "Authentication Key"

    pass


class DeployTool(HasTraits):
    "Deployment tool"

    pass


class Stack(HasTraits):
    "Stack of :class:`DeployTool`\ s"

    pass


