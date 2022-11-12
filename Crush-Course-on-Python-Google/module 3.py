# def multiplication_table(start, stop):
#     for x in range(1, stop+1):
#         for y in range(1, stop+1):
#             print(str(x * y), end=" ")
#         print()
#
#
# multiplication_table(1, 3)

# def counter(start, stop):
#     x = start
#     if start > stop:
#         return_string = "Counting down: "
#         while x >= stop:
#             return_string += str(x)
#             if x != stop:
#                 return_string += ","
#             x-=1
#
#     else:
#         return_string = "Counting up: "
#         while x <= stop:
#             return_string += str(x)
#             if x != stop:
#                 return_string += ","
#             x+=1
#
#     return return_string
#
#
# print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1))  # Should be "Counting down: 2,1"
# print(counter(5, 5))  # Should be "Counting up: 5"

# for x in range(10):
#     for y in range(x):
#         print(y)


def double_word(word):
    s=""
    if len(word) == 0:
        return 0
    else:
        s = "{}{}{}".format(word, word, str(len(word) * 2))
    return s

print(double_word("hello"))  # Should return hellohello10
print(double_word("abc"))  # Should return abcabc6
print(double_word(""))  # Should return 0