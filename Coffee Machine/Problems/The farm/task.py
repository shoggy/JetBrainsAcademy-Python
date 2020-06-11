n = int(input())
num = 0
animal = ''
if n >= 6769:
    num = n // 6769
    animal = 'sheep'
elif n >= 3848:
    num = n // 3848
    animal = 'cow'
elif n >= 1296:
    num = n // 1296
    animal = 'pig'
elif n >= 678:
    num = n // 678
    animal = 'goat'
elif n >= 23:
    num = n // 23
    animal = 'chicken'

if num >= 2 and animal != 'sheep':
    print(str(num) + ' ' + animal + 's')
elif num >= 1:
    print(str(num) + ' ' + animal)
else:
    print("None")
