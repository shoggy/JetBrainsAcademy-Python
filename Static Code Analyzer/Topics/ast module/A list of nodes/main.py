import ast

expression = "(34 + 6) * (23**2 - 7 + 45**2)"

# put your code here
tree = ast.parse(expression)
print(len(list(ast.walk(tree))))
