# write your code here
import argparse
import os
from collections import defaultdict, OrderedDict


def get_root_dir() -> str:
    parser = argparse.ArgumentParser(usage="Directory is not specified")
    parser.add_argument('root_dir', default=None, nargs='?')
    args = parser.parse_args()
    root = args.root_dir
    return root


def get_file_format() -> str:
    print("Enter file format:")
    return input()


def ask_is_descending_option() -> bool:
    msg = "Size sorting options:\n1. Descending\n2. Ascending"
    print(msg)
    while True:
        print("Enter a sorting option:")
        choice = input()
        if choice not in {'1', '2'}:
            print("Wrong option")
            continue
        else:
            return choice == '1'


def walk_dirs(root: str, filter_ext: str):
    files_map = defaultdict(list)
    for root, dirs, files in os.walk(root):
        for name in files:
            file = os.path.join(root, name)
            if file.endswith(filter_ext):
                files_map[os.path.getsize(file)].append(file)
    return {k: v for k, v in files_map.items() if len(v) > 1}


def main():
    root = get_root_dir()
    if root is None:
        print("Directory is not specified")
        exit()
    file_map = walk_dirs(root, get_file_format())
    is_desc = ask_is_descending_option()
    file_map = OrderedDict(sorted(file_map.items(), reverse=is_desc))
    for k, v in file_map.items():
        print(f"{k} bytes", *v, sep='\n')


if __name__ == '__main__':
    main()
