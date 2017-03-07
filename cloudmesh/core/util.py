
from dotdict import dotdict as _dotdict
import copy


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
            self[k] = v
