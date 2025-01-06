import requests
from bs4 import BeautifulSoup

"""
IMPORTANT NOTES - Why does urn has to start with cite2?
                - On line 169 of urls why id returns 3(?)
                - On line 580 of urls why title is These...

Root url - https://fragtrag1.upatras.gr/
Root urn - urn:cite2:fragtrag

Links_array - Array of links contains
    [0]: Comment if a poet exists (not required)
    [1]: Platform url attribute (not required)
    [2]: Platform name (not required)
    [3]: Name of poet (Required)
    [4]: Name of object (Required)
    [5]: Type of object or poem title (Optional)
    [6]: Source identifier (Optional)
"""

url = "https://fragtrag1.upatras.gr/exist/apps/fragtrag/indexc.html"

grab = requests.get(url)
soup = BeautifulSoup(grab.content, 'html.parser')

f = open('urls.txt', 'w')

links_array = []

true_index = 0

for i, link in enumerate(soup.find_all('a')):
    data = link.get('href')
    if '.xml' in data:
        links_array.append(data.split('/')[1:])
        if '#' in data:
            links_array[true_index][-1] = data.split('-')[-2]
            links_array[true_index].append(data.split('-')[-1])
        f.write(data)
        f.write('\n')
        true_index += 1

print(f'links_array: {links_array}')

f.close()
