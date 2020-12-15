import copy


def detect_copy():
    obj = [[1]]
    cp = copying_machine(obj)
    return "deep copy" if id(obj[0]) != id(cp[0]) else "shallow copy"
