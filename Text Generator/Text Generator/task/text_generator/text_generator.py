# Write your code here
from nltk.tokenize import regexp_tokenize
import nltk
from collections import defaultdict
from collections import Counter
import random


class Solution:

    def __init__(self, filename: str) -> None:
        self.token_list = self.read_corpus(filename)
        self.bigram_list = self.convert_to_bigrams()
        self.model = self.convert_to_markov_model()

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

    def convert_to_markov_model(self):
        # head -> Counter of tails
        result = defaultdict(Counter)
        for head, tail in self.bigram_list:
            result[head][tail] += 1
        return result

    def get_random_token(self):
        return random.choice(self.token_list)

    def get_next_random_token(self, prev: str):
        most_common = self.model[prev].most_common()
        population = [w for w, _ in most_common]
        weights = [cnt for _, cnt in most_common]
        return random.choices(population, weights, k=1)[0]

    def get_random_sentence(self, n: int):
        word = self.get_random_token()
        result = [word]
        for _ in range(n - 1):
            word = self.get_next_random_token(word)
            result.append(word)
        return ' '.join(result)


filename = input()
# filename = '../corpus.txt'
sol = Solution(filename)
# model = sol.model
# while True:
#     s = input().strip()
#     if 'exit' == s:
#         break
#     print(f'Head: {s}')
#     if s not in model:
#         print('The requested word is not in the model. Please input another word.')
#     else:
#         for w, cnt in model[s].most_common():
#             print(f'Tail: {w}\tCount: {cnt}')
for _ in range(10):
    print(sol.get_random_sentence(10))
