import pdftotext
import pandas as pd
import matplotlib.pyplot as plt

filename = r"./static/BP_2018.pdf"
with open(filename, 'rb') as f:
    pdf = pdftotext.PDF(f)


page_0 = pdf[0]



new_page = pdf[27]



text = "\n\n".join(pdf)  # 往字符串中添加\n\n

text = text.lower()




wordlist = pd.read_csv("./static/Sentiment_list_2018_ALL.csv")
for columns in wordlist.columns:
    wordlist[columns] = wordlist[columns].str.lower()




positive = wordlist["Positive"].dropna().tolist()
negative = wordlist['Negative'].dropna().tolist()
uncertainty = wordlist["Uncertainly"].dropna().tolist()
litigious = wordlist["Litigeious"].dropna().tolist()
constraining = wordlist["Constraining"].dropna().tolist()
all = list(set(positive + negative + uncertainty + litigious + constraining))

querywords = text.split()


resultword = [word for word in querywords if word.lower() in all]

positive_count = {}
for x in positive:
    positive_count[x] = resultword.count(x)

negative_count = {}
for x in negative:
    negative_count[x] = resultword.count(x)

uncertainty_count = {}
for x in uncertainty:
    uncertainty_count[x] = resultword.count(x)

litigious_count = {}
for x in litigious:
    litigious_count[x] = resultword.count(x)

constraining_count = {}
for x in constraining:
    constraining_count[x] = resultword.count(x)

all_count = {}
for x in all:
    all_count[x] = resultword.count(x)


positive_count = dict(sorted(positive_count.items(), reverse=True, key=lambda x: x[1]))
negative_count = dict(sorted(negative_count.items(), reverse=True, key=lambda x: x[1]))
uncertainty_count = dict(sorted(uncertainty_count.items(), reverse=True, key=lambda x: x[1]))
litigious_count = dict(sorted(litigious_count.items(), reverse=True, key=lambda x: x[1]))
constraining_count = dict(sorted(constraining_count.items(), reverse=True, key=lambda x: x[1]))
# all_count = dict(sorted(all_count.items(), reverse=True, key=lambda x:x[1]))


totals = {}

totals["postive"] = sum(positive_count.values())
totals["negative"] = sum(negative_count.values())
totals["uncertainty"] = sum(uncertainty_count.values())
totals["litigious"] = sum(litigious_count.values())
totals["constraining"] = sum(constraining_count.values())

sentiment = (totals["postive"] - totals["negative"]) / (totals["postive"] + totals["negative"])

print(sentiment)

fig = plt.figure(figsize=(8, 4), dpi=100)
plt.bar(list(totals.keys()), totals.values(), color=('g', 'r', 'darkgray', 'gold', 'blueviolet'))
plt.ylabel('Frequery', fontsize=10)
plt.title(f'Frequery of words by group')
plt.xticks(rotation=0)
plt.show()

n = 20

first_n_pairs = {k: positive_count[k] for k in list(positive_count)[:n]}
fig = plt.figure(figsize=(14, 4), dpi=100)
plt.bar(list(first_n_pairs.keys()), first_n_pairs.values(), color=('g'))
plt.ylabel('Frequery', fontsize=10)
plt.title(f'Frequery of {n} most common posttive words ')
plt.xticks(rotation=90)
plt.show()

first_n_pairs = {k: negative_count[k] for k in list(negative_count)[:n]}
fig = plt.figure(figsize=(14, 4), dpi=100)
plt.bar(list(first_n_pairs.keys()), first_n_pairs.values(), color=('g'))
plt.ylabel('Frequery', fontsize=10)
plt.title(f'Frequery of {n} most common negative words ')
plt.xticks(rotation=90)
plt.show()

first_n_pairs = {k: uncertainty_count[k] for k in list(uncertainty_count)[:n]}
fig = plt.figure(figsize=(14, 4), dpi=100)
plt.bar(list(first_n_pairs.keys()), first_n_pairs.values(), color=('g'))
plt.ylabel('Frequery', fontsize=10)
plt.title(f'Frequery of {n} most common uncertainty words ')
plt.xticks(rotation=90)
plt.show()

first_n_pairs = {k: constraining_count[k] for k in list(constraining_count)[:n]}
fig = plt.figure(figsize=(14, 4), dpi=100)
plt.bar(list(first_n_pairs.keys()), first_n_pairs.values(), color=('g'))
plt.ylabel('Frequery', fontsize=10)
plt.title(f'Frequery of {n} most common constraining words ')
plt.xticks(rotation=90)
plt.show()

