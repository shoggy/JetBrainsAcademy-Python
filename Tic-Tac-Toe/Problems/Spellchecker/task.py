dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()
ok = True
for word in words:
    if word not in dictionary:
        print(word)
        ok = False
if ok:
    print('OK')
