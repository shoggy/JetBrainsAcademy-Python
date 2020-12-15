def unpack(input_tuple):
    # your code here
    unpacked = []
    for x in input_tuple:
        if isinstance(x, tuple):
            unpacked += [*x]
        else:
            unpacked.append(x)
    return tuple(unpacked)
