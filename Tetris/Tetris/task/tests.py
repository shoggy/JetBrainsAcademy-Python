from hstest.stage_test import StageTest, List
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class Tetris(StageTest):
    def generate(self) -> List[TestCase]:
        return [
            TestCase(stdin='T',
                     attach=('',
                             '- - - -\n- - - -\n- - - -\n- - - -\n\n- 0 - -\n0 0 0 -\n- - - -\n- - - -\n\n'
                             '- 0 - -\n0 0 - -\n- 0 - -\n- - - -\n\n- - - -\n0 0 0 -\n- 0 - -\n- - - -\n\n'
                             '- 0 - -\n- 0 0 -\n- 0 - -\n- - - -\n\n- 0 - -\n0 0 0 -\n- - - -\n- - - -\n\n')),
            TestCase(stdin='J',
                     attach=('',
                             '- - - -\n- - - -\n- - - -\n- - - -\n\n- - 0 -\n- - 0 -\n- 0 0 -\n- - - -\n\n'
                             '- - - -\n0 0 0 -\n- - 0 -\n- - - -\n\n- 0 0 -\n- 0 - -\n- 0 - -\n- - - -\n\n'
                             '0 - - -\n0 0 0 -\n- - - -\n- - - -\n\n- - 0 -\n- - 0 -\n- 0 0 -\n- - - -\n\n')),
            TestCase(stdin='O',
                     attach=('',
                             '- - - -\n- - - -\n- - - -\n- - - -\n\n- - - -\n- 0 0 -\n- 0 0 -\n- - - -\n\n'
                             '- - - -\n- 0 0 -\n- 0 0 -\n- - - -\n\n- - - -\n- 0 0 -\n- 0 0 -\n- - - -\n\n'
                             '- - - -\n- 0 0 -\n- 0 0 -\n- - - -\n\n- - - -\n- 0 0 -\n- 0 0 -\n- - - -\n\n')),
            TestCase(stdin='Z',
                     attach=('',
                             '- - - -\n- - - -\n- - - -\n- - - -\n\n- - - -\n0 0 - -\n- 0 0 -\n- - - -\n\n'
                             '- - 0 -\n- 0 0 -\n- 0 - -\n- - - -\n\n- - - -\n0 0 - -\n- 0 0 -\n- - - -\n\n'
                             '- - 0 -\n- 0 0 -\n- 0 - -\n- - - -\n\n- - - -\n0 0 - -\n- 0 0 -\n- - - -\n\n'))

        ]

    def check(self, reply: str, attach):

        feedback, answer = attach

        board = answer.strip().split('\n\n')
        reply_board = reply.strip().split('\n\n')

        if len(board) != len(reply_board):
            return CheckResult.wrong(
                "A field with {0} grids is expected to be printed. Found {1} grids".format(len(board),
                                                                                           len(reply_board)))

        line = [grid.strip().split('\n') for grid in board]
        line_reply = [grid.strip().split('\n') for grid in reply_board]

        if len(line) != len(line_reply):
            return CheckResult.wrong(
                "A grid with {0} rows is expected to be printed. Found {1} rows".format(len(line), len(line_reply)))

        for j in range(len(line)):
            line_columns = [one.strip().split(' ') for one in line[j]]
            reply_columns = [one.strip().split(' ') for one in line_reply[j]]

            if len(line_columns) != len(reply_columns):
                return CheckResult.wrong(
                    f"A grid with {line_columns} columns is expected to be printed. Found {reply_columns} columns")

            for one_line in reply_columns:
                for symbol in one_line:
                    if symbol not in ('0', '-'):
                        return CheckResult.wrong(
                            "The field should contain zero (0) or short-dash (-) symbols. Found {}".format(symbol))

        for i in range(len(reply_board)):
            reply_board_per_line = reply_board[i].split('\n')
            answer_board_per_line = board[i].split('\n')

            for j in range(len(reply_board_per_line)):
                if reply_board_per_line[j] != answer_board_per_line[j]:
                    return CheckResult.wrong(
                        f"Wrong line {j + 1} in grid {i + 1}: Should be {answer_board_per_line[j]} instead of {reply_board_per_line[j]}")

        return CheckResult.correct()


if __name__ == '__main__':
    Tetris('tetris.game').run_tests()
