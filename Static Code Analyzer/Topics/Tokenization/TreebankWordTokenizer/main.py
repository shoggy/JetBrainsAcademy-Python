# put your python code here
from nltk.tokenize import TreebankWordTokenizer

twk = TreebankWordTokenizer()
text = input()
print(twk.tokenize(text))
