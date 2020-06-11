grade = int(input())
total = int(input())
res = grade / total * 100
if res >= 90:
    print("A")
elif res >= 80:
    print("B")
elif res >= 70:
    print("C")
elif res >= 60:
    print("D")
else:
    print("F")
