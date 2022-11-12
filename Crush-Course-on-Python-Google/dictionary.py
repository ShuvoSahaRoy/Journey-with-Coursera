# toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
# ___ # Epilogue starts on page 39
# ___ # Chapter 3 now starts on page 24
# ___ # What are the current contents of the dictionary?
# ___ # Is there a Chapter 5?

# wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
# for key,val in wardrobe.items():
#     for v in val:
#         print("{} {}".format(v, key))

# def email_list(domains):
#     emails = []
#     for domin, users in domains.items():
#         for user in users:
#             emails.append(user+'@'+domin)
#     return (emails)
#
#
# print(email_list(
#     {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
#      "hotmail.com": ["bruce.wayne"]}))

def groups_per_user(group_dictionary):
    user_groups = {}
    group=[]

    for group in group_dictionary.keys():
        # Now go through the users in the group
        for users in group_dictionary[group]:
            lst = []
            for group in group_dictionary.keys():
                if users in group_dictionary[group] and users not in lst:
                    lst.append(group)
            user_groups[users] = lst
    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
        "public":  ["admin", "userB"],
        "administrator": ["admin"] }))
