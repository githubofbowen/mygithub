# # # # d = {'a': 1, "b": 2, "c":4}
# # # # print(list(d))
# # # # print(sorted(d.items(),key=lambda x:x[1],reverse=False))
# # # # list_a = [1, 2, 3, 4, 5, 6]
# # # # print(list_a[-1:5])
# # #
#
#
#
#
# from nltk.tokenize import word_tokenize
# sentence = "I love nature language processing"
# tokens = word_tokenize(sentence)
# print(tokens)
#
#
# #
#
# sentence = 'The brown fox is quick and he is jumping over the lazy dog'
# import nltk
# tokens = nltk.word_tokenize(sentence)
# tagged_sent = nltk.pos_tag(tokens)
# print(tagged_sent)


a = [1, 2, 3, 3]

b = [4, 5, 6, 4, 6]



all = list(set(a+b))
print(all)
# print(all)