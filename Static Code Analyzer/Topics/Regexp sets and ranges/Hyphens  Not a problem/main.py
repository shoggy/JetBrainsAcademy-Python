import re

# your code here
word = input()
print(re.match(r"\b.+-.+\b", word) is not None)
