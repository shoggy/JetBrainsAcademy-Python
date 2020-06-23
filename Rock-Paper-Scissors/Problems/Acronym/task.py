# read test.txt
fin = open('test.txt', mode='r')
for line in fin:
    print(line[0])
fin.close()
