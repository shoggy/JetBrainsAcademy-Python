import numpy as np

array = np.array([[-34, 2, 0],
                  [0, -4, 123],
                  [-201, 0, -3]], dtype=np.int64)

a = int(input())
b = int(input())
print(array[a].astype(np.str_))
print(array[b].astype(np.float64))
