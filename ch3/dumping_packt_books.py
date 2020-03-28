import urllib.request
from urllib.request import Request
import ssl

from bs4 import BeautifulSoup
url = "https://www.packtpub.com/all-products/all-books"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urllib.request.urlopen(req,context=ctx)
soup_packtpage = BeautifulSoup(page)


soup_packtpage.find_all('div', class_=['product', 'details', 'product-item-details'], limit=1)

items = soup_packtpage.find_all('div', class_=['product', 'details', 'product-item-details'])
for item in items:
  title = item.find('a', class_='product-item-link').get_text()
  pubdate = item.find('div', class_='date-of-publication').get_text()
  price = item.find('span', class_=['price-container price-final_price tax weee'])
  print('Title: ' + title.strip())
  print('Publishing Date: ' + pubdate.strip())
  print('Price: ' + price.find('span', class_='price', recursive=True).get_text())
