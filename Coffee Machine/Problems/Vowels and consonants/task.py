vowels = list('aeiou')
s = input()
for c in s:
    if not c.isalpha():
        break
    if c in vowels:
        print('vowel')
    else:
        print('consonant')
