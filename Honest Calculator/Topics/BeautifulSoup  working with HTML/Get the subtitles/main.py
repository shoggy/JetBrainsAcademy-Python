import requests

from bs4 import BeautifulSoup

idx = int(input())
r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.find_all('h2')[idx].text)
