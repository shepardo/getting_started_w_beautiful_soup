import re
from bs4 import BeautifulSoup

email_id_example = """<br/>
<div>The below HTML has the information that has email ids.</div>
abc@example.com
<div>xyz@example.com</div>
<span>foo@example.com</span>
"""

email_soup = BeautifulSoup(email_id_example,"lxml")
emailid_regexp = re.compile("\w+@\w+\.\w+")
first_email_id = email_soup.find(text=emailid_regexp)
print(first_email_id)


email_ids_limited = email_soup.find_all(text=emailid_regexp,limit=2)
print(email_ids_limited)

