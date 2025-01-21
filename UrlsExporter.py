"""
UrlsExporter.py: A tool to export and process URLs. This script includes functions
to handle URL extraction, processing, and storage  into different formats.
Modify and customize the script based on specific needs.
Copyright (C) 2025, Iraklis Markelis

UrlsExporter is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

UrlsExporter is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

File name: UrlsExporter.py
Version: 1.00
Author: Iraklis Markelis
License: GPL-3.0 License
Date created: 10/1/2025
Date last modified: 10/1/2025
Python Version: 3.9.1
Email: imarkelis@upatras.gr
"""

import requests
from bs4 import BeautifulSoup

class UrlsExporter:
    """
    Handles the process of exporting URLs for given data entities (web pages).

    This class is designed to enable efficient exportation of URLs related to
    specific data entities. Through its methods, it facilitates storage and
    retrieval, providing an organized mechanism for URL handling. It can be
    extended or adapted as necessary to suit specific requirements.
    """

def __init__(self, url, filename):
    """
    :param self: Reference to the current instance of the class.
    :param url: The root url to be scanned
    :type url: str
    :param filename: The urls file name to be exported
    :type filename: str
    """
    self.url = url
    self.filename = filename
    self.urls_array = []
    self.path_elements_array = []

def extract_links(self):
    grab = requests.get(self.url)
    soup = BeautifulSoup(grab.content, 'html.parser')
    true_index = 0

    for i, link in enumerate(soup.find_all('a')):
        data = link.get('href')
        if '.xml' in data:
            self.urls_array.append(data)
            self.path_elements_array.append(data.split('/')[1:])
            if '#' in data:
                self.path_elements_array[true_index][-1] = data.split('-')[-2]
                self.path_elements_array[true_index].append(data.split('-')[-1])
            true_index += 1

    return self.path_elements_array, self.urls_array

def create_urls_file(self):
    f = open(self.filename, 'w')
    for i, link in enumerate(self.urls_array):
        f.write(link)
        f.write('\n')
    f.close()
