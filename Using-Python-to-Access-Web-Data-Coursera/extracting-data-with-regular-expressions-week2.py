import re

with open('regex_sum_728433.txt','r') as file:
    file = file.read()
    nums = re.findall('[0-9]+',file)
    sum=0
    for num in nums:
        sum+= int(num)
    print(sum)