# read sums.txt
fin = open('sums.txt', mode='r')
for line in fin:
    a, b = [int(x) for x in line.split()]
    print(a + b)
fin.close()
