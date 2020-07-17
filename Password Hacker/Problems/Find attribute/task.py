from lxml import etree

root = etree.fromstring(input())
print(root.get(input()))
