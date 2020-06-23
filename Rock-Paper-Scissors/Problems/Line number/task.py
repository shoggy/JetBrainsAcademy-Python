# read sample.txt and print the number of lines
fin = open('sample.txt', mode='r')
print(len(fin.readlines()))
fin.close()
