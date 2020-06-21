text = input()
# text = text.lower()
words = text.split()
for word in words:
    # finish the code here
    if word.upper().startswith('HTTPS://') \
            or word.upper().startswith('HTTP://') \
            or word.upper().startswith('WWW.'):
        print(word)
