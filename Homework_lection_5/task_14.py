# Given a list of words, create a dictionary 
# where the keys are the words and the values are their lengths, using dictionary comprehension.

list_of_words = ["Arsenal", "Chelsea", "Manchester United", "Barcelona", "Real Madrid"]

words_len_dict = {word: len(word) for word in list_of_words}

print(words_len_dict)