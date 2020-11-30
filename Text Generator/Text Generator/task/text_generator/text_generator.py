# Write your code here
import random
import re
from collections import Counter
from collections import defaultdict

import nltk
from nltk.tokenize import regexp_tokenize


class Solution:

    def __init__(self, filename: str) -> None:
        self.token_list = self.read_corpus(filename)
        self.bigram_list = self.convert_to_bigrams()
        self.model = self.convert_to_markov_model()
        self.first_token_list = self.generate_first_token_list()

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

    def generate_first_token_list(self):
        return [x for x in self.token_list if re.match(r'[A-Z].*[^.!?]$', x) is not None]

    def is_sentence_end_token(self, token: str):
        return re.match(r'.*[.!?]$', token) is not None

    def get_first_random_token(self):
        return random.choice(self.first_token_list)

    def get_next_random_token(self, prev: str):
        most_common = self.model[prev].most_common()
        population = [w for w, _ in most_common]
        weights = [cnt for _, cnt in most_common]
        return random.choices(population, weights, k=1)[0]

    def get_random_sentence(self, at_least: int):
        word = self.get_first_random_token()
        result = [word]
        for _ in range(at_least - 1):
            word = self.get_next_random_token(word)
            result.append(word)
        while not self.is_sentence_end_token(word):
            word = self.get_next_random_token(word)
            result.append(word)
        return ' '.join(result)


filename = input()
# filename = '../corpus.txt'
sol = Solution(filename)
for _ in range(10):
    print(sol.get_random_sentence(5))
