import requests

from bs4 import BeautifulSoup

letter = 'S'
# letter = 'L'
url = input()
# url = 'http://web.archive.org/web/20201201053628/https://www.who.int/health-topics'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

result = []
for elem in soup.select('a[href*=topics],a[href*=entity]'):
    if elem.text.startswith(letter) and len(elem.text) > 1:
        result.append(elem.text)
print(result)
