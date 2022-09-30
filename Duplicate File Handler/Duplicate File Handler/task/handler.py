# write your code here
import argparse
import os


def get_root_dir() -> str:
    parser = argparse.ArgumentParser(usage="Directory is not specified")
    parser.add_argument('root_dir', default=None, nargs='?')
    args = parser.parse_args()
    root = args.root_dir
    return root


def walk_dirs(root: str):
    for root, dirs, files in os.walk(root):
        for name in files:
            print(os.path.join(root, name))


def main():
    root = get_root_dir()
    if root is None:
        print("Directory is not specified")
        exit()
    walk_dirs(root)


if __name__ == '__main__':
    main()
