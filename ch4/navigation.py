from bs4 import BeautifulSoup
from bs4.element import NavigableString

html_markup = """<div class="ecopyramid">
<ul id="producers">
<li class="producerlist">
<div class="name">plants</div>
<div class="number">100000</div>
</li>
<li class="producerlist">
<div class="name">algae</div>
<div class="number">100000</div>
</li>
</ul>
</div>"""

soup = BeautifulSoup(html_markup,"lxml")
producer_entries = soup.ul
print(producer_entries)

first_producer = producer_entries.li
print(first_producer)

for string in first_producer.strings:
  print(string)

print(type(soup.contents))

for tag in soup.contents:
  print(tag.name)

for child in producer_entries.contents:
  print(child)


print(type(soup.children))

for tag in soup.children:
  print(tag.name)

print(len(list(soup.descendants)))

for tag in soup.descendants:
  if isinstance(tag, NavigableString):
    print(tag)
  else:
    print(tag.name)

producer_entries = soup.ul
print(producer_entries.parent)

html_tag = soup.html
print(html_tag.parent.name)

print(soup.parent)

third_div = soup.find_all("div")[2]

for parent in third_div.parents:
  print(parent.name)


soup = BeautifulSoup(html_markup)
first_producer = soup.find("li")
second_producer = first_producer.next_sibling
second_producer_name = second_producer.div.string
print(second_producer_name)

print(second_producer.previuos_sibling)

print(first_producer.previous_sibling)

for previous_sibling in second_producer.previous_siblings:
  print(previous_sibling.name)


first_producer = soup.li
print(first_producer.next_element)

second_div = soup.find_all("("div")[")[1]
print(second_div.previous_element)
