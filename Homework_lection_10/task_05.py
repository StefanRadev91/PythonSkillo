def count_words(s):

    words = s.split()

    return len(words)

input_string = input("Enter a string: ")
word_count = count_words(input_string)
print(f"The number of words in the string is: {word_count}")