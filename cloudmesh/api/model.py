"""
This module provides the model API for components
"""

from traits.api import HasTraits


class Node(HasTraits):

    pass


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


