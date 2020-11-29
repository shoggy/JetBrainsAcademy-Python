from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from collections import Counter, defaultdict
from random import sample


def preprocess() -> dict:
    # tokenize
    with open("test/corpus.txt", "r", encoding="utf-8") as f:
        corpus = f.read().split()

    # create n-grams
    ngrams = list()
    for i in range(len(corpus) - 1):
        ngrams.append((corpus[i], corpus[i + 1]))

    # get frequencies
    freq = defaultdict(Counter)
    for head, tail in ngrams:
        freq[head][tail] += 1
    return freq


class TextGeneratorTests(StageTest):

    def generate(self):
        with open("test/corpus.txt", "r", encoding="utf-8") as f:
            corpus = f.read().split()
        test_input1 = "test/corpus.txt\nKing\nJon\nNight\nKlangenfurt\nexit\n"
        test_input2 = "test/corpus.txt\n" + '\n'.join(sample(corpus, 3)) + "\nexit\n"
        test_input3 = "test/corpus.txt\n" + '\n'.join(sample(corpus, 3)) + "\nNotInCorpus\nexit\n"
        return [
            TestCase(stdin=test_input1, attach=test_input1),
            TestCase(stdin=test_input2, attach=test_input2),
            TestCase(stdin=test_input3, attach=test_input3)
        ]

    def check(self, reply, attach):
        model = preprocess()

        # check output
        if not reply:
            return CheckResult.wrong("The output cannot be empty! Make sure to output the results of your program!")

        entries = reply.split('Head: ')
        if len(entries) == 1:
            return CheckResult.wrong("Make sure that every entry starts with the line: 'Head: [head]'")

        for entry in entries:
            lines = entry.split('\n')

            # check if the "head" is in the model: if not, it will stay None
            control = None
            if lines[0] in model:
                control = model[lines[0]]
            results = lines[1:-2]
            for res in results:
                if control is not None:
                    if len(res.split()) != 4:
                        return CheckResult.wrong(
                            "Every tail entry should have the format: 'Tail: [tail] Count: [count]'")
                    tail, count = res.split()[1], res.split()[3]
                    if tail not in control:
                        return CheckResult.wrong("Invalid tail: every tail should be part of the entry that corresponds to the given head!!")
                    try:
                        if int(count) != control[tail]:
                            return CheckResult.wrong(
                                "Incorrect count in model. Make sure that repetitions are recorded as count.")
                    except ValueError:
                        return CheckResult.wrong("Count should be castable to int.")
                else:
                    if ("Key Error" or "key error" or "Key error" or "keyerror" or "KeyError") not in res:
                        return CheckResult.wrong(
                            "Error messages should contain the types of errors (Index Error, Type Error, Key Error etc.)")

        return CheckResult.correct()


if __name__ == '__main__':
    TextGeneratorTests('text_generator.text_generator').run_tests()
