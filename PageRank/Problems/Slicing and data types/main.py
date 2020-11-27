import numpy as np

array = np.array([[212, 215, 434, 2, 0],
                  [6, 447, 0, 4, 143],
                  [10, 478, 601, 602, 3]], dtype=np.float64)

a = int(input())
b = int(input())
print(array[a, ::b].astype(np.int8))
