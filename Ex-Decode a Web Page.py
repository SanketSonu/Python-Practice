"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times.
"""

import requests
from bs4 import BeautifulSoup

urls = []
r = requests.get('https://www.nytimes.com')
r_html = r.text
soup = BeautifulSoup(r_html)
for h in soup.find_all('a'):
    link = h.attrs['href']
    urls.append(link)

for i in urls:
    if "2018" in i:
        print(i)
