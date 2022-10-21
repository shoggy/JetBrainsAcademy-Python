import ast

result = []

tree = ast.parse(code)
for i in ast.walk(tree):
    if isinstance(i, ast.Call):
        result.append(i.func.id)
print(result)
