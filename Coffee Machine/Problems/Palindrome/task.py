# put your python code here
s = input()
for i in range(len(s) // 2):
    if s[i] != s[-i - 1]:
        print("Not palindrome")
        break
else:
    print("Palindrome")
