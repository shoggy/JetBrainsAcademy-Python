import ast


class ImportVisitor(ast.NodeVisitor):
    def visit_Import(self, node):
        for n in node.names:
            print(n.name)


tree = ast.parse(code)

t = ImportVisitor().visit(tree)
