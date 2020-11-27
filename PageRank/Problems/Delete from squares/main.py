a = int(input())
if a not in squares:
    print("There is no such key")
else:
    print(squares[a])
    del squares[a]
