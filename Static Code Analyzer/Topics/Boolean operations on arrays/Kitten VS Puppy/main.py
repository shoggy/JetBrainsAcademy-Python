import numpy as np

lst_1 = []
for i in input().split():
    lst_1.append(int(i))
lst_2 = input().split()
lst_3 = input().split()

# finish the code here, help the Kitten and the Puppy!
predicate = np.array(lst_1)
positive = np.array(lst_2)
negative = np.array(lst_3)
print(*np.where(predicate < 0, negative, positive), sep='\n')
