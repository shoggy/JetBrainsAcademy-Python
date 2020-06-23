# write your code here
with open('salary.txt', 'r') as fin, \
        open('salary_year.txt', 'w') as fout:
    for line in fin:
        print(int(line.strip()) * 12, file=fout)
