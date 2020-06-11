n = int(input())
if n < 1:
    print("no army")
elif n < 10:
    print("few")
elif n < 50:
    print("pack")
elif n < 500:
    print("horde")
elif n < 1000:
    print("swarm")
else:
    print("legion")
