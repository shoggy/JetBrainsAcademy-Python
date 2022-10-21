# write your code here
import argparse
import ast
import itertools
import os.path
import re
from _ast import FunctionDef, arg, Name
from abc import ABC, abstractmethod
from typing import Any

APPLICABLE_EMPTY_LINES_BEFORE_CODE = 2
INDENT_MULTIPLIER = 4
MAX_LEN = 79


class LintError(ABC):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message

    def describe(self) -> str:
        return f"{self.code} {self.message}"

    @abstractmethod
    def is_ok(self, line: str) -> bool:
        pass

    @staticmethod
    def remove_str_literals(line):
        return re.sub(r"'.*'", '', line)


class S001TooLong(LintError):

    def __init__(self):
        super().__init__("S001", "Too long")

    def is_ok(self, line: str) -> bool:
        return len(line) <= MAX_LEN


class S002IndentationMultiplier(LintError):

    def __init__(self):
        super().__init__("S002", "Indentation is not a multiple of four")

    def is_ok(self, line: str) -> bool:
        space_len = len(line) - len(line.lstrip())
        return space_len % INDENT_MULTIPLIER == 0


class S003UnnecessarySemicolon(LintError):
    def __init__(self):
        super().__init__("S003", "Unnecessary semicolon after a statement")

    def is_ok(self, line: str) -> bool:
        line_without_str_literals = self.remove_str_literals(line)
        comment_pos = line_without_str_literals.find('#')
        semicolon_pos = line_without_str_literals.find(';')
        return semicolon_pos == -1 \
               or -1 < comment_pos <= semicolon_pos


class S004LessSpacesBeforeInlineComment(LintError):

    def __init__(self):
        super().__init__("S004", "Less than two spaces before inline comments")

    def is_ok(self, line: str) -> bool:
        semicolon_pos = line.find('#')
        return semicolon_pos == -1 \
               or semicolon_pos == 0 \
               or line[:semicolon_pos].endswith(' ' * 2)


class S005ToDoFound(LintError):

    def __init__(self):
        super().__init__("S005", "TODO found")

    def is_ok(self, line: str) -> bool:
        line_without_str_literals = self.remove_str_literals(line)
        comment_pos = line_without_str_literals.find('#')
        todo_pos = line_without_str_literals.lower().find('todo', comment_pos)
        return comment_pos == -1 \
               or todo_pos == -1


class S006MoreBlankLinesPrecedingCode(LintError):

    def __init__(self):
        super().__init__("S006", "More than two blank lines preceding a code line")
        self.empty_lines_counter = 0

    def is_ok(self, line: str) -> bool:
        if line.strip() == '':
            self.empty_lines_counter += 1
            return True
        else:
            res = self.empty_lines_counter <= APPLICABLE_EMPTY_LINES_BEFORE_CODE
            self.empty_lines_counter = 0
            return res


class S007TooManySpacesAfterConstructionName(LintError):

    def __init__(self, construct_name):
        super().__init__("S007", f"Too many spaces after '{construct_name}'")
        self.construct_name = construct_name

    def is_ok(self, line: str) -> bool:
        pattern = re.compile(r" *\b" + self.construct_name + r"\b( +)(\w+)(\(\w*\))?:")
        match = pattern.match(line)
        return match is None \
               or len(match.group(1)) == 1


class S008ClassNameShouldBeCamelCase(LintError):
    def __init__(self):
        super().__init__("S008", "Class name class_name should be written in CamelCase")

    def is_ok(self, line: str) -> bool:
        pattern = re.compile(r" *\bclass\b( +)(\w+)(\(\w*\))?:")
        match = pattern.match(line)
        return match is None \
               or re.match(r"([A-Z][a-z]*)+", match.group(2)) is not None


class S009FunctionNameShouldBeSnameCase(LintError):
    def __init__(self):
        super().__init__("S009", "Function name function_name should be written in snake_case")

    def is_ok(self, line: str) -> bool:
        pattern = re.compile(r" *\bdef\b( +)(\w+)(\(\w*\))?:")
        match = pattern.match(line)
        return match is None \
               or re.match(r"_*([a-z]+_?)+_*", match.group(2)) is not None


class AstErrors(LintError):
    def __init__(self, code: str, message: str):
        super().__init__(code, message)

    def is_ok(self, line: str) -> bool:
        pass


class Ololo(ast.NodeVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.errors: set[tuple[int, LintError]] = set()

    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        args: list[list[arg]] = [node.args.args, node.args.posonlyargs, node.args.kwonlyargs]
        for i in itertools.chain(*args):
            arg_name = i.arg
            if re.match(r"_*([a-z]+_?)+_*", arg_name) is None:
                self.errors.add((i.lineno, AstErrors("S010", f"Argument name '{i.arg}' should be snake_case")))
        for i in node.args.defaults:
            if isinstance(i, ast.List):
                self.errors.add((i.lineno, AstErrors("S012", "Default argument value is mutable")))
        for nd in ast.iter_child_nodes(node):
            self.visit(nd)

    def visit_Name(self, node: Name) -> Any:
        if isinstance(node.ctx, ast.Store) and re.match(r"_*([a-z]+_?)+_*", node.id) is None:
            self.errors.add((node.lineno, AstErrors("S011", f"Variable '{node.id}' in function should be snake_case")))


ERRORS: tuple = (
    S001TooLong(),
    S002IndentationMultiplier(),
    S003UnnecessarySemicolon(),
    S004LessSpacesBeforeInlineComment(),
    S005ToDoFound(),
    S006MoreBlankLinesPrecedingCode(),
    S007TooManySpacesAfterConstructionName('class'),
    S007TooManySpacesAfterConstructionName('def'),
    S008ClassNameShouldBeCamelCase(),
    S009FunctionNameShouldBeSnameCase(),
)


def check_file(file_path) -> [tuple[int, LintError]]:
    errors: [tuple[int, LintError]] = []
    with open(file_path, mode="rt", encoding="utf-8") as fin:
        for line_num, line in enumerate(fin, start=1):
            for check in ERRORS:
                if not check.is_ok(line.rstrip()):
                    errors.append((line_num, check))

    with open(file_path, mode="rt", encoding="utf-8") as fin:
        tree = ast.parse(fin.read())
    tree_walker = Ololo()
    tree_walker.visit(tree)
    extensions = sorted(tree_walker.errors, key=lambda x: x[0])
    errors.extend(extensions)
    return errors


def print_errors(path, errors):
    for error in errors:
        print(f"{path}: Line {error[0]}: {error[1].describe()}")


def get_file_path() -> str:
    parser = argparse.ArgumentParser(usage="Directory is not specified")
    parser.add_argument('root_dir', default=None, nargs='?')
    args = parser.parse_args()
    root = args.root_dir
    return root


def walk_dirs(root: str) -> list[str]:
    filelist = []
    for root, dirs, files in os.walk(root):
        for name in files:
            file = os.path.join(root, name)
            if file.endswith(".py"):
                filelist.append(file)
    return sorted(filelist)


def main():
    file_path = get_file_path()
    if file_path is None:
        print("Directory is not specified")
        exit()
    files = None
    if os.path.isdir(file_path):
        files = walk_dirs(file_path)
    elif os.path.isfile(file_path):
        files = [file_path, ]

    for f in files:
        errors = check_file(f)
        print_errors(f, errors)


if __name__ == '__main__':
    main()
