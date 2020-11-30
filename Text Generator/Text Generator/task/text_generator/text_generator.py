# Write your code here
import random
import re
from collections import Counter
from collections import defaultdict

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
        return [(f'{a} {b}', c) for a, b, c in zip(token_list[:-2], token_list[1:-1], token_list[2:])]
        # return list(nltk.bigrams(token_list))

    def print_bigram_stastics(self):
        print(f'Number of bigrams: {len(self.bigram_list)}')

    def convert_to_markov_model(self):
        # head -> Counter of tails
        result = defaultdict(Counter)
        for head, tail in self.bigram_list:
            result[head][tail] += 1
        return result

    def generate_first_token_list(self):
        return [x for x, _ in self.bigram_list if re.match(r'[A-Z][^.!?]*\s.*', x) is not None]

    def is_sentence_end_token(self, token: str):
        return re.match(r'.*[.!?]$', token) is not None

    def get_first_random_token(self):
        return random.choice(self.first_token_list)

    def get_next_random_token(self, prev: str):
        most_common = self.model[prev].most_common()
        population = [w for w, _ in most_common]
        weights = [cnt for _, cnt in most_common]
        return random.choices(population, weights, k=1)[0]

    def get_random_sentence(self, at_least: int) -> str:
        first, second = self.get_first_random_token().split()
        result = [first, second]
        next_token = ''
        for _ in range(at_least - 2):
            next_token = self.get_next_random_token(f'{first} {second}')
            first = second
            second = next_token
            result.append(second)
        while not self.is_sentence_end_token(next_token):
            next_token = self.get_next_random_token(f'{first} {second}')
            first = second
            second = next_token
            result.append(second)
        return ' '.join(result)


filename = input()
# filename = '../corpus.txt'
sol = Solution(filename)
for _ in range(10):
    print(sol.get_random_sentence(5))
