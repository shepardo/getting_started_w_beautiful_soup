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
