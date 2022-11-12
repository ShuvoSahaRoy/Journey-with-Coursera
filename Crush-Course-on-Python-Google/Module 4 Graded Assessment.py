# /////////////////////////////////////////
# def format_address(address_string):
#     # Declare variables
#     words = address_string.split()
#     # Separate the address string into parts
#     house_no = words[0]
#     # Traverse through the address parts
#     i=1
#     rd=""
#     for i in range(i,len(words)):
#         if i+1<len(words):
#             rd = rd+ words[i]+" "
#         else:
#             rd = rd + words[i]
#
#     # Determine if the address part is the
#     # house number or part of the street name
#
#     # Does anything else need to be done
#     # before returning the result?
#
#     # Return the formatted string
#     return "house number {} on street named {}".format(house_no,rd)
#
#
# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"
#
# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"
#
# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"

# ///////////////////////////////////////
# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)

# ////////////////////
# animal = "Hippopotamus"
# print(animal[3:6])
# print(animal[-5])
# print(animal[10:])

# /////////////////
# def highlight_word(sentence, word):
#     s= sentence.replace(word,word.upper())
#     return s
#
# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))

#/ ////////////////////
# def combine_guests(guests1, guests2):
#     for key, val in guests1.items():
#         guests2[key] = val
#     return guests2
#
# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
#
# print(combine_guests(Rorys_guests, Taylors_guests))

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    letter = letter.lower()
    if letter.isalpha():
      if letter in result:
        result[letter] += 1
      else:
        result[letter] = 1
    # Add or increment the value in the dictionary
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}