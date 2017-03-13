from __future__ import absolute_import

import copy

import sqlalchemy as SA
from traits import trait_types as TT


_traits2sql = {
    TT.Bool: SA.Boolean,
    TT.Str: SA.String,
    TT.String: SA.String,
    TT.UUID: SA.String,
}


def traits2sql(defns=None):
    defns = defns or dict()

    t2s = copy.copy(_traits2sql)
    t2s.update(defns)

    return t2s
