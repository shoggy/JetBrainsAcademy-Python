# the object_list has already been defined
# write your code here
from collections.abc import Hashable

d = dict()
for x in object_list:
    if isinstance(x, Hashable):
        t = x.__hash__()
        d[t] = d.get(t, 0) + 1
acc = sum((x for x in d.values() if x > 1))
print(acc)
