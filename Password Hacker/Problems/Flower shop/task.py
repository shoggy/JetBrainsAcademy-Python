import itertools

for i in range(1, 4):
    for c in itertools.combinations(flower_names, i):
        print(c)
