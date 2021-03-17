import requests
from bs4 import BeautifulSoup, Tag


WIKI_HOST = "https://wiki.biligame.com"

res = requests.get("https://wiki.biligame.com/pcr/%E9%95%9C%E5%8D%8E")
# print(res.text)
html = BeautifulSoup(res.text, 'lxml')
html = html.find(title="角色讨论/攻略")
tables = html.find_all('table')
table1 = tables[0]
if '角色攻略' in table1.th.text:
    for li in table1.find_all('li'):
        print(li.a['title'])
        print(WIKI_HOST + li.a['href'])

for table in tables[1:]:
    print(table.text)
