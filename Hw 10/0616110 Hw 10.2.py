from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
site = 'http://www.shopping.com/camera/products?CLT=SAS&KW=camera'
request = urllib.request.urlopen(site).read()
soup = BeautifulSoup(request, 'html.parser')
#print(soup.prettify())

#print(soup.find_all('img'))

links = soup.find_all('img', class_='imgZoomUrl60')
for items in links:
    print(items.get('src'))

