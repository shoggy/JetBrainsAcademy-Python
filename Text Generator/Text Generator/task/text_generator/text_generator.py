# Write your code here
from nltk.tokenize import regexp_tokenize
import nltk


class Solution:

    def __init__(self, filename: str) -> None:
        self.token_list = self.read_corpus(filename)
        self.bigram_list = self.convert_to_bigrams()

    def read_corpus(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            return regexp_tokenize(text, '\\S+')

    def print_corpus_statistics(self):
        token_list = self.token_list
        print(f'Corpus statistics')
        print(f'All tokens: {len(token_list)}')
        print(f'Unique tokens: {len(set(token_list))}')

    def convert_to_bigrams(self):
        token_list = self.token_list
        # return [b for b in zip(token_list[:-1], token_list[1:])]
        return list(nltk.bigrams(token_list))

    def print_bigram_stastics(self):
        print(f'Number of bigrams: {len(self.bigram_list)}')


filename = input()
# filename = '../corpus.txt'
sol = Solution(filename)
sol.print_bigram_stastics()
bigrams = sol.bigram_list
bigrams_size = len(bigrams)
while True:
    s = input().strip()
    if 'exit' == s:
        break
    try:
        idx = int(s)
        if idx >= bigrams_size or idx < -bigrams_size:
            print('Index Error. Please input a value that is not greater than the number of all bigrams.')
            continue
        bigram = bigrams[idx]
        print(f'Head: {bigram[0]}\tTail: {bigram[1]}')
    except ValueError:
        print('Type Error. Please input an integer.')
        continue
