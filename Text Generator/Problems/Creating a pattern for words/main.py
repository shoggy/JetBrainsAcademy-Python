from nltk.tokenize import regexp_tokenize

text = input()
n = int(input())
print(regexp_tokenize(text, "[A-z']+")[n])
