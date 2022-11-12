# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# newfilenames = []
#
# for file in filenames:
#   if '.hpp' in file:
#     newfilenames.append(file[:-2])
#   else:
#     newfilenames.append(file)
#
# print(newfilenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# def pig_latin(text):
#     say = ""
#     # Separate the text into words
#     words = text.split()
#     for word in words:
#         # Create the pig latin word and add it to the list
#         lst= word[0]
#         word = word[1:]+ lst+'ay'
#         say= say + word +" "
#         # Turn the list back into a phrase
#     return say
#
#
# print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4, "r"), (2, "w"), (1, "x")]
#     # Iterate over each of the digits in octal
#     for digit in [int(n) for n in str(octal)]:
#         # Check for each of the permissions values
#         for value, letter in value_letters:
#             if digit >= value:
#                 result += letter
#                 digit -= value
#             else:
#                 result += '-'
#     return result
#
#
# print(octal_to_string(755))  # Should be rwxr-xr-x
# print(octal_to_string(644))  # Should be rw-r--r--
# print(octal_to_string(750))  # Should be rwxr-x---
# print(octal_to_string(600))  # Should be rw-------

# def group_list(group, users):
#     print(group + ": ", end="")
#     s = ""
#     i = 0
#     for user in users:
#         if i < len(users)-1:
#             s = s + user + ',' + " "
#         i+=1
#         if i==len(users):
#             s= s+ user
#     final = s
#     return final
#
#
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", ""))  # Should be "Users:"

# def guest_list(guests):
#     for guest in guests:
#         print("{} is {} years old and works as {}".format(guest[0],guest[1],guest[2]))
#
#
# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
#
# """
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
# """
