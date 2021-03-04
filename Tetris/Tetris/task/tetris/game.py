# Write your code here
import copy
import math


def print_matrix(mt):
    size = int(math.sqrt(len(mt)))
    for row in [mt[i:i + size] for i in range(0, len(mt), size)]:
        print(' '.join(map(str, row)))
    print()


def add_symbols(mt, letter):
    res = copy.copy(mt)
    for i in letter:
        res[i] = 0
    return res


null_mt = ['-'] * 16

segs = {
    'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
    'S': [[6, 5, 9, 8], [5, 9, 10, 14]],
    'Z': [[4, 5, 9, 10], [2, 6, 5, 9]],
    'L': [[1, 5, 9, 10], [6, 10, 9, 8], [5, 6, 10, 14], [9, 5, 6, 7]],
    'J': [[2, 6, 10, 9], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]],
    'O': [[5, 6, 10, 9]],
    'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]
}

inp = input()
print_matrix(null_mt)
letter_segs = segs[inp]
for i in range(5):
    print_matrix(add_symbols(null_mt, letter_segs[i % len(letter_segs)]))
