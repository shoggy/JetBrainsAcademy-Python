s = input()
res = ''
for i in s:
    if i.isupper():
        res += '_' + i.lower()
    else:
        res += i
print(res)
