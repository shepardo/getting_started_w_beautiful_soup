from bs4 import BeautifulSoup

with open("ecologicalpyramid.html","r") as ecological_pyramid:
  soup = BeautifulSoup(ecological_pyramid,"lxml")

all_tertiaryconsumers = \
  soup.find_all(class_="tertiaryconsumerlist")

for tertiaryconsumer in all_tertiaryconsumers:
  print(tertiaryconsumer.div.string)

