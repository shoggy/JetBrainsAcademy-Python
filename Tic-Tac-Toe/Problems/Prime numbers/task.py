prime_numbers = [x for x in range(2, 1000) if all(x % y for y in range(2, x))]
