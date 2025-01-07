import requests
from bs4 import BeautifulSoup

"""
IMPORTANT NOTES - Why does urn has to start with cite2?
                - On line 169 of urls why id returns 3(?)
                - On line 580 of urls why title is These...

Root url - https://fragtrag1.upatras.gr/
Root urn - urn:cite2:fragtrag

Links_array - Array of links contains
    [0]: Reference to eXist-db [The Open Source Native XML Database] (not required)
    [1]: Platform url attribute (not required)
    [2]: Platform name (not required)
    [3]: Name of poet (Required)
    [4]: Name of object (Required)
    [5]: Type of object or poem title (Optional)
    [6]: Source identifier (Optional)
"""

url = "https://fragtrag1.upatras.gr/exist/apps/fragtrag/indexc.html"
root_urn = "urn:cite2:fragtrag"

grab = requests.get(url)
soup = BeautifulSoup(grab.content, 'html.parser')

f = open('urls.txt', 'w')

links_array = []
urls_array = []
urns_array = []

true_index = 0

for i, link in enumerate(soup.find_all('a')):
    data = link.get('href')
    if '.xml' in data:
        urls_array.append(data)
        links_array.append(data.split('/')[1:])
        if '#' in data:
            links_array[true_index][-1] = data.split('-')[-2]
            links_array[true_index].append(data.split('-')[-1])
        f.write(data)
        f.write('\n')
        true_index += 1

f.close()

# Code to build URNs

for i, link in enumerate(links_array):
    urns_array.append(root_urn)
    urns_array[i] += ":" + links_array[i][3]
    urns_array[i] += "." + links_array[i][4]
    # Check if it is an object or a title
    # Afterward check if title exists
    if links_array[i][6] == 'title':
        urns_array[i] += "." + links_array[i][6]
        urns_array[i] += ":" + links_array[i][5]
    else:
        urns_array[i] += "." + links_array[i][5]
        urns_array[i] += ":" + links_array[i][6]

f = open('Docs/urns.txt', 'w')

for i, url in enumerate(urls_array):
    data = url + '\t' + urns_array[i]
    f.write(data)
    f.write('\n')

print(f'links_array: {links_array}')
print(f'urns_array: {urns_array}')


