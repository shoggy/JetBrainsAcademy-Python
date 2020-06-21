val = [int(x) for x in input()]
print([sum(val[:x]) for x in range(1, len(val) + 1)])
