scores = input().split()
# put your python code here
mis = 0
res = 0
for c in scores:
    if c == 'C':
        res += 1
    elif c == 'I':
        mis += 1
    if mis >= 3:
        print("Game over")
        break
else:
    print("You won")
print(res)
