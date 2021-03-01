import json

import requests
from bs4 import BeautifulSoup as bs


def work():
    user_url = input('Input the URL:\n')
    res = 'Invalid movie page!'
    try:
        r = requests.get(user_url)
        if r.status_code == 200:
            soup = bs(r.content, 'html.parser')
            resp_title = json.loads("".join(soup.find('script', {'type': 'application/ld+json'}).contents))['name']
            resp_description = soup.select_one('.summary_text').text.strip()
            if resp_title and resp_description:
                res = json.dumps({'title': resp_title, 'description': resp_description})
    finally:
        return res


print(work())
