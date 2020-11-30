import requests

from bs4 import BeautifulSoup

word = input()
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')

for p in soup.find_all('p'):
    if word in p.text:
        print(p.text)
        break
