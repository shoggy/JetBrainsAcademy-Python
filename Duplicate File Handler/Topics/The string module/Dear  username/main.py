import string

# put your code here
username = input()
template = string.Template("Dear $username! It was really nice to meet you. "
                           "Hopefully, you have a nice day! See you soon, $username!")
result = template.substitute(username=username)
print(result)
