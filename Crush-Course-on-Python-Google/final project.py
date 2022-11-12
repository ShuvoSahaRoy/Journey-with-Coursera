f="The fol^^lowing are the graphical (non-control) characters defined by ISO 8859-1 (1987).  Descriptions in words aren't all that helpful, but they're the best we can do in text.  A graphics file illustrating the character set should be available from the same archive as this"

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

uninteresting_words_upper = [word.capitalize() for word in uninteresting_words]
for letter in punctuations:
    f = f.replace(letter,'')

count={}

for word in f.split():
    if word not in uninteresting_words and word not in uninteresting_words_upper:
        if word not in count:
            count[word] = 0
        count[word] += 1
print(count)