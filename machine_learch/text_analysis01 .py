import matplotlib.pyplot as plt
from unidecode import unidecode

from string import digits
from string import ascii_lowercase
from string import punctuation

# open file
filename = "war_and_peace_full.txt"
with open(filename, encoding="utf8") as file:
    text = file.read().lower().strip()
print(type(text), "位置一")



#  unicode 是一种统一的字符    ASCII 中英文占一个字节，中文占用两个字节
#  unicode   中英文都是双字节  处理效率快
text = unidecode(text)
print(type(text), '位置二')



letter_count = {}
for x in ascii_lowercase:
    letter_count[x] = text.count(x)
# 统计text  字符串中  每一个小写 字母在文本中出现的个数
print(letter_count)

# chart letters
fig = plt.figure(figsize=(80, 14), dpi=100)
plt.bar(list(letter_count.keys()), letter_count.values(), color='g')
plt.xlabel('letter', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.title('Frequency of letters with "war and peace"')
plt.show()
print(1)
# count digits

digit_count = {}
for x in digits:
    digit_count[x] = text.count(x)

fig = plt.figure(figsize=(8, 4), dpi=100)
plt.bar(list(digit_count.keys()), digit_count.values(), color='g')
plt.xlabel('Numbers', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.title('Frequency of numbers with "war and peace"')
plt.show()
print(2)
# count punctuation

punctuation_count = {}
for x in punctuation:
    punctuation_count[x] = text.count(x)



fig = plt.figure(figsize=(8, 4), dpi=100)
plt.bar(list(punctuation_count.keys()), punctuation_count.values(), color='g')
plt.xlabel('Punctuation', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.title('Frequency of punctuation with "war and peace"')
plt.show()
print(3)
# remove punctuation and words
special_punctuation = "-/"
for s in special_punctuation:
    text = text.replace(s, "")
for d in digits:
    text = text.replace(d, "")

# create list of unique words
wordlist = []
words = text.split()
for word in words:
    if word not in wordlist:
        wordlist.append(word)
wordlist.sort()

# count the words and sort
wordcount = {}
for word in wordlist:
    wordcount[word] = words.count(word)
sortedcount = dict(sorted(wordcount.items(), reverse=True, key=lambda x: x[1]))



# plot the top n most frequent words
n = 30
First_n_pairs = {k: sortedcount[k] for k in list(sortedcount)[:n]}




fig = plt.figure(figsize=(14, 4), dpi=100)
plt.bar(list(First_n_pairs.keys()), First_n_pairs.values(), color="g")
plt.xlabel('Word', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.title(f"Frequency of {n} most common words within 'war and peace'")
plt.xticks(rotation=90)
plt.show()
print(4)
##############################################################
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

import nltk

filename = "war_and_peace_full.txt"
with open(filename, encoding="utf8") as file:
    text = file.read().lower().strip()

from unidecode import unidecode

text = unidecode(text)

special_punctuation = "-/"
for s in special_punctuation:
    text = text.replace(s, "")
for p in special_punctuation:
    text = text.replace(p, "")
for d in digits:
    text = text.replace(d, "")

nltk_words = word_tokenize(text)

# create list of unique words
nltk_wordlist = []
for word in nltk_words:
    if word not in nltk_wordlist:
        nltk_wordlist.append(word)
nltk_wordlist[word] = nltk_words.count(word)

nltk_wordcount = {}
for word in nltk_wordlist:
    nltk_wordcount[word] = nltk_words.count(word)
nltk_sortedcount = dict(sorted(nltk_wordcount.items(), reverse=True, key=lambda x: x[1]))

# plot the top n most frequent words
n = 50
First_n_pairs = {k: nltk_sortedcount[k] for k in list(nltk_sortedcount)[:n]}

fig = plt.figure(figsize=(14, 4), dpi=100)
plt.bar(list(First_n_pairs.keys()), First_n_pairs.values(), color="g")
plt.xlabel('Word', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.title(f"Frequency of {n} most common words within 'war and peace'")
plt.xticks(rotation=90)
plt.show()
print(5)
###################################################
stopwords = stopwords.words('english')
no_stopwords = {}
for key, value in sortedcount.items():
    if key not in stopwords:
        no_stopwords[key] = value

# plot the top n most frequent words
n = 30
First_n_pairs = {k: no_stopwords[k] for k in list(no_stopwords)[:n]}

fig = plt.figure(figsize=(14, 4), dpi=100)
plt.bar(list(First_n_pairs.keys()), First_n_pairs.values(), color="g")
plt.xlabel('Word', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.title(f"Frequency of {n} most common words within 'war and peace'")
plt.xticks(rotation=90)
plt.show()
print(6)
stopwords.append("said")  # remove a particular word, rerunning again

##################################################
lemmatizer = WordNetLemmatizer()
lemma_words = []

nltk_words = word_tokenize(text)
for word in nltk_words:
    lemma_words.append(lemmatizer.lemmatize(word))

lemma_wordlist = []
for word in lemma_words:
    if word not in lemma_wordlist:
        lemma_wordlist.append(word)
lemma_wordlist.sort()

lemma_wordcount = {}
for word in lemma_wordlist:
    lemma_wordcount[word] = lemma_words.count(word)
lemma_sortedcount = dict(sorted(lemma_wordcount.items(), reverse=True, key=lambda x: x[1]))

stopwords = stopwords.words('english')
stopwords.append("wa")
no_stopwords = {}
for key, value in lemma_sortedcount.items():
    if key not in stopwords:
        no_stopwords[key] = value

n = 30
First_n_pairs = {k: no_stopwords[k] for k in list(no_stopwords)[:n]}

fig = plt.figure(figsize=(14, 4), dpi=100)
plt.bar(list(First_n_pairs.keys()), First_n_pairs.values(), color="g")
plt.xlabel('Word', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.title(f"Frequency of {n} most common words within 'war and peace'")
plt.xticks(rotation=90)
plt.show()
print(7)