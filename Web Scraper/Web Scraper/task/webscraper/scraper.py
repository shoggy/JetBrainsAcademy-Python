import string
from pathlib import Path

import requests
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
from furl import furl
import re


def is_article_body(tag: Tag) -> bool:
    return tag.name == "div" and re.match(r'article.*body', tag.get('class', [''])[0])


def save_page(user_url: str, file_name: str, page_num):
    r = requests.get(user_url)
    if r.status_code == 200:
        with open(Path(f'./Page_{page_num}', file_name), mode='wb') as fout:
            elems = bs(r.content, 'html.parser').find(is_article_body)
            fout.write(elems.text.strip().encode('utf-8'))


def work(page_num, req_art_type='News'):
    Path(f'./Page_{page_num}').mkdir(parents=True, exist_ok=True)
    f = furl(f'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={page_num}')
    r = requests.get(str(f))
    articles = []
    if r.status_code == 200:
        soup = bs(r.content, 'html.parser')
        for art in soup.select('article'):
            art_type = art.select_one('span[data-test="article.type"]')
            if art_type and art_type.get_text(strip=True) == req_art_type:
                link = art.select_one('a[data-track-action="view article"]')
                fc = f.copy()
                fc.path.set(link['href'])
                link_href = str(fc)
                link_name = link.text.translate(str.maketrans(' ', '_', string.punctuation)) + '.txt'
                articles.append(link_name)
                save_page(link_href, link_name, page_num)
    print(f'Saved articles: {articles}')


pg_num = int(input())
art_type = input()
for i in range(1, pg_num + 1):
    work(i, art_type)
