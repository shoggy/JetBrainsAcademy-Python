import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--number")
args = parser.parse_args()
print(args.number)
