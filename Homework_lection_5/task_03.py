# Given a list of words, create a new list containing the lengths of each word.
# 3.1. Given a list of words, create a new dictionary mapping every word to it's length.

list_of_words = ["Arsenal", "Chelsea", "Manchester United", "Barcelona", "Real Madrid"]

len_of_list_of_words = []
for word in list_of_words:
    len_of_list_of_words.append(len(word))

print(len_of_list_of_words)

dict_list_of_words = {index: value for index, value in enumerate(list_of_words)}
dict_len_of_words = {index: value for index, value in enumerate(len_of_list_of_words)}

print(dict_list_of_words)
print(dict_len_of_words)

mapped_dict = {}
for key, word in dict_list_of_words.items():
    word_length = dict_len_of_words.get(key)
    mapped_dict[word] = word_length

print(mapped_dict)

