from __future__ import absolute_import

from dotdict import dotdict as _dotdict


class Dotdict(_dotdict):

    def __init__(self, d):
        """
        Recursively created a dotdict

        :param dict d: dictionary
        :returns: dotted dict
        :rtype: :class:`Dotdict`
        """

        for k in d.keys():
            v = d[k]
            if isinstance(v, dict):
                v = Dotdict(v)
            elif isinstance(v, list):
                v = map(Dotdict, v)
            self[k] = v

