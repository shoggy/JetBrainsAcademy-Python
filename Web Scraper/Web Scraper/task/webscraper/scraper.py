from bs4 import BeautifulSoup as bs
import requests
import string
from furl import furl


def save_page(user_url: str, file_name: str):
    r = requests.get(user_url)
    if r.status_code == 200:
        with open(file_name, mode='wb') as fout:
            fout.write(bs(r.content, 'html.parser').select_one('.article__body').text.strip().encode('utf-8'))


def work(user_url):
    f = furl(user_url)
    r = requests.get(user_url)
    articles = []
    if r.status_code == 200:
        soup = bs(r.content, 'html.parser')
        for art in soup.select('article'):
            art_type = art.select_one('span[data-test="article.type"]')
            if art_type and art_type.get_text(strip=True) == 'News':
                link = art.select_one('a[data-track-action="view article"]')
                fc = f.copy()
                fc.path.set(link['href'])
                link_href = str(fc)
                link_name = link.text.translate(str.maketrans(' ', '_', string.punctuation)) + '.txt'
                articles.append(link_name)
                save_page(link_href, link_name)
    print(f'Saved articles: {articles}')


print(work('https://www.nature.com/nature/articles'))
