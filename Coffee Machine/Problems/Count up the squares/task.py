# put your python code here
res = 0
s = 0
while True:
    n = int(input())
    s += n
    res += n * n
    if s == 0:
        print(res)
        break
