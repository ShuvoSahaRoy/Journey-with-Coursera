import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Split the string only at the first occurrence:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)