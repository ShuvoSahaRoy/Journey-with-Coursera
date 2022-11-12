def convert(line):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in line:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct


# def calculate_frequencies(file_contents):
#     # Here is a list of punctuations and uninteresting words you can use to process your text
#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
#                            "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
#                            "they", "them", \
#                            "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
#                            "been", "being", \
#                            "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
#                            "where", "how", \
#                            "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
#                            "can", "will", "just"]
#
#     # LEARNER CODE START HERE
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]
f = open("file.txt")
lines = f.readlines()
count={}
for line in lines:
    line= convert(line)
    words = line.split(" ")
    for word in words:
        if word not in uninteresting_words:
            if word not in count:
                count[word] = 0
            count[word]+=1
# count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1],reverse=True)}
# for k,v in count.items():
#     print(k,v)

print(count)