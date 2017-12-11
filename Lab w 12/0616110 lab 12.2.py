from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import re
url = 'https://docs.python.org/3/library/index.html'
f = urllib.request.urlopen(url).read()

soup = BeautifulSoup(f, 'html.parser')

#print(soup.prettify())

topics = soup.find_all("li", class_= 'toctree-l2')

for items in topics:
    print(items.text.strip())



