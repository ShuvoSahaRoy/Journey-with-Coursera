import json
from urllib.request import urlopen

url = input("Enter - ")
uh = urlopen(url)
data = uh.read()


info = json.loads(data)
print('User count:', len(info))
sum = 0
l= info['comments']
for item in l:
    sum+= int(item['count'])

print(sum)