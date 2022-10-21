# put your code here

cur_sum = 0
cur_len = 0
while True:
    curr = int(input())
    if curr == 55:
        break
    cur_sum += curr
    cur_len += 1
print(cur_len)
print(cur_sum)
print(round(cur_sum / cur_len))
