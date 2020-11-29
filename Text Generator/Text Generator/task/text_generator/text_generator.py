# Write your code here
from nltk.tokenize import regexp_tokenize


class Solution:
    def read_corpus(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            return regexp_tokenize(text, '\\S+')

    def print_corpus_statistics(self, token_list: list):
        print(f'Corpus statistics')
        print(f'All tokens: {len(token_list)}')
        print(f'Unique tokens: {len(set(token_list))}')


sol = Solution()
filename = input()
# filename = '../corpus.txt'
token_list = sol.read_corpus(filename)
token_list_size = len(token_list)
sol.print_corpus_statistics(token_list)
while True:
    s = input().strip()
    if 'exit' == s:
        break
    try:
        idx = int(s)
        if idx >= token_list_size:
            print('Index Error')
            continue
        print(token_list[idx])
    except ValueError:
        print('Type Error')
        continue
