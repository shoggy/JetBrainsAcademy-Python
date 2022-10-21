import re

word = input()
# your code here
print(bool(re.match(r'\bthe\b', word)))
