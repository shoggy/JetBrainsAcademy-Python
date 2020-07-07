rank = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
acc = 0
for _ in range(6):
    acc += rank.get(input().strip(), 0)
print(acc / 6)
