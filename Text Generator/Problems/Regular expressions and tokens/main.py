from nltk.tokenize import regexp_tokenize

text = input()
print(regexp_tokenize(text, r"[A-z'\-]+"))
