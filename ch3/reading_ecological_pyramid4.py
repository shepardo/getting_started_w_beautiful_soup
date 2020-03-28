from bs4 import BeautifulSoup

with open("ecologicalpyramid.html","r") as ecological_pyramid:
  soup = BeautifulSoup(ecological_pyramid,"lxml")

producers= soup.find(id='producers')
next_siblings = producers.find_next_siblings()
print(next_siblings)
