# create your dictionary here
from collections.abc import Hashable

objects_dict = {x: hash(x) for x in objects if isinstance(x, Hashable)}
