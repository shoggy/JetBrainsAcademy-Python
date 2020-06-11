res = ''
m = 0
s = input()
while s != 'MEOW':
    t = s.split()
    if int(t[1]) > m:
        m = int(t[1])
        res = t[0]
    s = input()
print(res)
