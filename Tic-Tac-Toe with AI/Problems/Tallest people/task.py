def tallest_people(**kwargs):
    height = max(kwargs.values())
    s = [k for k, v in kwargs.items() if v == height]
    s.sort()
    for t in s:
        print(f"{t} : {height}")
