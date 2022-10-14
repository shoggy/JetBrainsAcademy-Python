# write your code here
import re
from abc import ABC, abstractmethod

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


ERRORS: tuple[LintError] = (
    S001TooLong(),
    S002IndentationMultiplier(),
    S003UnnecessarySemicolon(),
    S004LessSpacesBeforeInlineComment(),
    S005ToDoFound(),
    S006MoreBlankLinesPrecedingCode(),
)


def main():
    errors: [tuple[int, LintError]] = []
    file_path = input()
    with open(file_path, mode="rt", encoding="utf-8") as fin:
        for line_num, line in enumerate(fin, start=1):
            for check in ERRORS:
                if not check.is_ok(line.rstrip()):
                    errors.append((line_num, check))
    for error in errors:
        print(f"Line {error[0]}: {error[1].describe()}")


if __name__ == '__main__':
    main()
