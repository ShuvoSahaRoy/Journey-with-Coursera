import re
txt = "The rain in Spain"
# Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)

# Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)

# Check if "ain" is present at the end of a WORD:
x = re.findall(r"ain\b", txt)
print(x)

# Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)
print(x)

# Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)

# Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", txt)
print(x)

# Return a match at every no-digit character:
x = re.findall("\D", txt)
print(x)

# Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)

# Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", txt)
print(x)

# Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
print(x)

# Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
print(x)

# Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
print(x)

# Check if the string has any characters between a and n:
x = re.findall("[a-n]", txt)
print(x)

# Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
print(x)

# Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[0123]", txt)
print(x)

txt = "8 times before 11:45 AM"
#Check if the string has any digits:
x = re.findall("[0-9]+", txt)
print(x)

# Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt)
print(x)

# Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt)
print(x)

#Check if the string has any + characters:
x = re.findall("[+]", txt)
print(x)