import re
import requests
from bs4 import BeautifulSoup

import xml.etree.ElementTree as ET

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

# Load the XML file
xml_parse = ET.parse('concordance.xml')
root = xml_parse.getroot()


url = "https://fragtrag1.upatras.gr/exist/apps/fragtrag/indexc.html"
root_urn = "urn:fragtrag"

grab = requests.get(url)
soup = BeautifulSoup(grab.content, 'html.parser')

f = open('urls.txt', 'w')

links_array = []
urls_array = []
urns_array = []
tagged_urns_array = []

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

# ToDo: Some remarks made by Andreas on exported strings
for i, link in enumerate(links_array):

    # A complete name is created for each type of object
    if links_array[i][5] == 'test':
        links_array[i][5] = 'testimonium'
    elif links_array[i][5] == 'frag':
        links_array[i][5] = 'fragment'
    elif links_array[i][5] == 'rep':
        links_array[i][5] = 'report'

    tagged_urns_array.append('<urn>')
    urns_array.append(root_urn)
    urns_array[i] += ":" + links_array[i][3]
    urns_array[i] += "." + links_array[i][4]
    # Check if it is an object or a title
    # Afterward check if title exists
    if links_array[i][6] == 'title':
        urns_array[i] += "." + links_array[i][6]
        # urns_array[i] += ":" + links_array[i][5].lower()
        # Dashes are SEO friendly and more readable
        urns_array[i] += ":" + re.sub(r"_", "-", links_array[i][5].lower())
    else:
        urns_array[i] += "." + links_array[i][5].lower()
        # ID is represented by only by numbers and letters
        urns_array[i] += ":" + re.sub("[^A-Za-z0-9]+", "", links_array[i][6]).lower()
    tagged_urns_array[i] += urns_array[i] + '</urn>'
f = open('urns.txt', 'w')

for i, url in enumerate(urls_array):
    data = url + '\t' + urns_array[i]
    f.write(data)
    f.write('\n')

f.close()

# Iterate through all fragtrag elements
for fragtrag in root.findall('.//fragtrag'):
    # Get the value of the corresp attribute
    corresp_value = fragtrag.get('corresp')
    index = None
    # Create a new text node with the corresp value and additional string
    # new_text = f"{corresp_value} {string_to_add}"

    try:
        # Find the index of the search string
        print(f'corresp_value: {corresp_value}')
        index = [i for i, url in enumerate(urls_array) if corresp_value == ("#" + url.split('#')[1])]
        print(f"The index of '{corresp_value}' is: {index}")
    except ValueError:
        print(f"'{corresp_value}' is not in the urls_array.")

    # Add the new text to the fragtrag element
    if index:
        fragtrag.text = (fragtrag.text or '') + tagged_urns_array[index[0]]

# Write the modified XML back to a file
xml_parse.write('modified_file.xml', encoding='utf-8', xml_declaration=True)

# print(f'links_array: {links_array}')
# print(f'urns_array: {urns_array}')
