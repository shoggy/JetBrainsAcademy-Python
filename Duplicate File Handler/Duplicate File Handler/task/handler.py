# write your code here
import argparse
import hashlib
import itertools
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


def ask_if_want_to_find_dups() -> bool:
    msg = "Check for duplicates?\n"
    available_opts = {'yes', 'no'}
    answer = input(msg)
    while answer not in available_opts:
        print('Wrong option')
        answer = input(msg)
    return answer == 'yes'


def walk_dirs(root: str, filter_ext: str):
    files_map = defaultdict(list)
    for root, dirs, files in os.walk(root):
        for name in files:
            file = os.path.join(root, name)
            if file.endswith(filter_ext):
                files_map[os.path.getsize(file)].append(file)
    return {k: v for k, v in files_map.items() if len(v) > 1}


def get_hash(file_path: str):
    hash_md5 = hashlib.md5()
    with open(file_path, mode="rb") as fis:
        for chunk in iter(lambda: fis.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_dups_by_hash(file_paths: list[str]):
    grouped = {k: list(v) for k, v in itertools.groupby(sorted(file_paths, key=get_hash), get_hash)}
    # pprint.pprint(grouped)
    t = {k: v for k, v in grouped.items() if len(v) > 1}
    return t


def ask_if_want_to_delete_dups() -> bool:
    msg = "Delete files?\n"
    available_opts = {'yes', 'no'}
    while True:
        answer = input(msg)
        if answer in available_opts:
            return answer == 'yes'
        else:
            print('Wrong option')


def ask_file_numbers_to_delete(n: int) -> list[int]:
    msg = "Enter file numbers to delete:\n"
    while True:
        answer = input(msg)
        try:
            file_nums = set(int(i) for i in answer.split(' '))
            if len(file_nums) > 0 and max(file_nums) <= n:
                return list(file_nums)
        except:
            print('Wrong option')


def delete_files_and_count_size(dupd_files_list: list[tuple], file_nums_to_delete: list[int]) -> int:
    freed_size = 0
    for delete_file_num in file_nums_to_delete:
        file_num = delete_file_num - 1
        file_description = dupd_files_list[file_num]
        freed_size += file_description[1]
        os.remove(file_description[0])
    return freed_size


def main():
    root = get_root_dir()
    if root is None:
        print("Directory is not specified")
        exit()
    file_map = walk_dirs(root, get_file_format())
    is_desc = ask_is_descending_option()
    # dict<size:int, list<str>>
    file_map = OrderedDict(sorted(file_map.items(), reverse=is_desc))
    for k, v in file_map.items():
        print(f"{k} bytes", *v, sep='\n')
    is_find_dups = ask_if_want_to_find_dups()
    if is_find_dups:
        dupd_files_list = []
        for file_size, files_list in file_map.items():
            dups = get_dups_by_hash(files_list)
            if len(dups) > 0:
                print(f"{file_size} bytes", )
                for hash_code, file_paths in dups.items():
                    print(f"Hash: {hash_code}")
                    for file_path in file_paths:
                        dupd_files_list.append((file_path, file_size))
                        print(f"{len(dupd_files_list)}. {file_path}")
        is_delete_dups = ask_if_want_to_delete_dups()
        if is_delete_dups:
            file_nums_to_delete = ask_file_numbers_to_delete(len(dupd_files_list))
            freed_size = delete_files_and_count_size(dupd_files_list, file_nums_to_delete)
            print(f"Total freed up space: {freed_size} bytes")


if __name__ == '__main__':
    main()
