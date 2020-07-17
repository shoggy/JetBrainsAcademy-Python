from lxml import etree

root = etree.fromstring(input())
for i in root:
    print(i.text)
