a = int(input().strip())
s = sum(a.to_bytes(2, byteorder="little"))
print(s)
