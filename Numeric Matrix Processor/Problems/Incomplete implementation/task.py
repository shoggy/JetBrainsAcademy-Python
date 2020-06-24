def startswith_capital_counter(names):
    acc = 0
    for name in names:
        if len(name) > 0 and name[0].isupper():
            acc += 1
    return acc
