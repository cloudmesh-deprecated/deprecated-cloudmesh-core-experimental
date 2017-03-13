
from traits.api import Adapter, HasTraits, adapt, provides


class IProvider(Interface):

    def boot(self, properties):
        "Boot a vm"


class Node(HasTraits):

    name = Str


@provides(IProvider)
class Node2IProvider(Adapter):

