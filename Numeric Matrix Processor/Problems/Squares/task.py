def sq_sum(a, *args):
    res = a * a
    for x in args:
        res += x * x
    return res
