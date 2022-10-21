import ast

# put your code here
u = input()
res = ast.literal_eval(u)
print(type(res))
