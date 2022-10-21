from nltk.tokenize import sent_tokenize
from nltk.tokenize import regexp_tokenize

text = input()
n = int(input())
sentence_for_tokenization = sent_tokenize(text)[n]
print(regexp_tokenize(sentence_for_tokenization, "[A-z']+"))
