from collections import Counter

text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

cnt = Counter(text.split())
result = cnt.most_common(int(input()))
for k, v in result:
    print(k, v)
