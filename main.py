import requests
from bs4 import BeautifulSoup

url = "https://fragtrag1.upatras.gr/exist/apps/fragtrag/indexc.html"

grab = requests.get(url)
soup = BeautifulSoup(grab.content, 'html.parser')

# rs = (grequests.get(u) for u in url)

"""
rs = grequests.get(url)

for r in grequests.map(rs):
    print(f'r.url: {r.url}')
"""

f = open('urls.txt', 'w')

for link in soup.find_all('a'):
    data = link.get('href')
    if '.xml' in data:
        f.write(data)
        f.write('\n')

f.close()
