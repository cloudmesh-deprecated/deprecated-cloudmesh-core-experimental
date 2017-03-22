from cloudmesh.api.provider import Provider


class Cloud(Provider):
    """A high-level wrapper for a cloud :class:`Provider`.

    Methods may accept and return implementations of the resources.

    """

    def __init__(self, provider):
        self._provider = provider

    @property
    def provider(self):
        """The implementation provider

        This is here as developer documentation and to provide
        low-level access to the provider.

        It is not intended to be accessed outside an instance of this
        class.
        """

        return self._provider
