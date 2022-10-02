# write your code here
class LintError:
    def __init__(self, code: str, message: str = ''):
        self.code = code
        self.message = message

    def describe(self) -> str:
        return f"{self.code} {self.message}"


ERRORS = {
    "S001": LintError("S001", "Too long"),
}


def main():
    errors: [tuple[int, LintError]] = []
    file_path = input()
    with open(file_path, mode="rt", encoding="utf-8") as fin:
        for line_num, line in enumerate(fin, start=1):
            if len(line) > 79:
                errors.append((line_num, ERRORS["S001"]))
    for error in errors:
        print(f"Line {error[0]}: {error[1].describe()}")


if __name__ == '__main__':
    main()
