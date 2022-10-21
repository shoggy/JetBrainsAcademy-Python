s = input()
substr = 'old'
print(max(s.find(substr), s.rfind(substr)))
