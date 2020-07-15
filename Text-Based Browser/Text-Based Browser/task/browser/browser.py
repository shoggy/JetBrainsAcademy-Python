import os
import sys
from collections import deque
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

init(autoreset=True)

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


# write your code here

class Browser:
    def __init__(self, dir_path: str):
        self.dir_path = Path(dir_path)
        os.makedirs(self.dir_path, exist_ok=True)
        self.downloads = set()
        self.history_back = deque()
        self.history_forth = deque()
        self.stored = {'nytimes.com': nytimes_com,
                       'bloomberg.com': bloomberg_com}

    @staticmethod
    def is_valid_url(url: str) -> bool:
        return '.' in url

    @staticmethod
    def normalize_url(url: str) -> str:
        if not url.startswith("http://") \
                and not url.startswith("https://"):
            return f"https://{url}"

    @staticmethod
    def normalize_content(content: str) -> str:
        soup = BeautifulSoup(content, "html.parser")
        result_set = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                                    'a', 'ul', 'ol', 'li'])
        return '\n'.join([Fore.BLUE + x.text if x.name == 'a' else x.text
                          for x in result_set])

    def save_to_file(self, file_name: str, content: str):
        file_path = self.dir_path / file_name
        file_path.write_text(content, encoding='utf-8')

    def print_file(self, file_name: str):
        file_path = self.dir_path / file_name
        with open(file_path, mode="r") as fin:
            for line in fin:
                print(line, end='')

    def process_page(self, url: str) -> bool:
        if url in self.downloads:
            self.print_file(url)
            return True
        elif not self.is_valid_url(url):
            print("error in url")
            return False
        else:
            # try to "download"
            content = requests.get(self.normalize_url(url)).text
            normalized_content = self.normalize_content(content)
            file_name = url[:url.rindex('.')]
            self.save_to_file(file_name, normalized_content)
            self.downloads.add(file_name)
            print(normalized_content)
            return True

    def command(self, cmd: str):
        if cmd == 'back':
            if len(self.history_back) > 1:
                # move current page to forth
                if len(self.history_forth) == 0:
                    self.history_forth.append(self.history_back.pop())
                prev = self.history_back.pop()
                # move previous to forth
                self.history_forth.append(prev)
                self.process_page(prev)
        else:
            if len(self.history_forth) > 0:
                self.history_back.append(self.history_forth.pop())
                self.history_forth.clear()
            if self.process_page(cmd):
                self.history_back.append(cmd)


args = sys.argv
if len(args) < 2:
    raise AttributeError("one CLI argument expected")

browser = Browser(args[1])

while True:
    user_inp = input().strip()
    if user_inp == "exit":
        break
    else:
        browser.command(user_inp)
