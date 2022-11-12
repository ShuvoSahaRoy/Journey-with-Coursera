from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl,re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum=0
nums= []
string = ""
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    string+= str(tag)

nums = re.findall('[0-9]+', string)
for num in nums:
    sum+= int(num)
print(sum)

