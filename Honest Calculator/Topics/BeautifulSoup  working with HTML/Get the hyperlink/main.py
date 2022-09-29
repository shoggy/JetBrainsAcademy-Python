import requests

from bs4 import BeautifulSoup

act = int(input())
page_url = input()

r = requests.get(page_url)
soup = BeautifulSoup(r.content, 'html.parser')

a = soup.find_all('a')
# print(list(a)[act].get('href'))
print(a[act - 1].get('href'))
