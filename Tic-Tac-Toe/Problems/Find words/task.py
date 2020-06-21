words = input().split()
filtered_words = [x for x in words if x.endswith('s')]
print("_".join(filtered_words))
