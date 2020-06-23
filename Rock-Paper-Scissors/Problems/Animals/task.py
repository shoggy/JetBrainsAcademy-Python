# read animals.txt
# and write animals_new.txt
fin = open('animals.txt', mode='r')
fout = open('animals_new.txt', mode='w', encoding='utf-8')
for line in fin:
    fout.write(line.strip() + ' ')
fout.close()
fin.close()
