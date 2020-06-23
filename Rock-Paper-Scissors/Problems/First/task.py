# read test_file.txt
fin = open("test_file.txt", mode='r', encoding='utf-16')
print(fin.readline())
fin.close()
