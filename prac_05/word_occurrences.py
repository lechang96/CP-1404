count_words = {}

text = input("Enter a text:")
words = text.split()

for word in words:
    counts = count_words.get(word,0)
    count_words[word] = counts + 1

words = list(count_words.keys())
words.sort()

for word in words:
    print("{} : {}".format(word, count_words[word]))