from __future__ import absolute_import

from munch import munchify

__all__ = ['Dotdict']


# The `Munch()` constructor does not recursively "munchify" a dict.
# To do so, we use the `munchify` "smart constructor"

Dotdict = munchify
