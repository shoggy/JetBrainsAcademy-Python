from collections.abc import Hashable


def solve(obj):
    return not isinstance(obj, Hashable)
