# Write a function that counts the frequency of each word in a given string 
# (copy the first paragraph of an online article, for example) and returns a dict with the result.
import re

def count_word_frequencies(input_string):
    input_string = input_string.lower()
    
    input_string = re.sub(r'[^\w\s]', '', input_string)
    
    words = input_string.split()
    
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

python_article = """Python articles
Python is a popular programming language used to
 develop solutions in a variety of spaces. 
 The language can be used to create websites, 
 process data, build robots, and solve other problems. 
 Its simple syntax, resembling the English language, 
 makes it very beginner friendly and a great first language to learn. 
 The tutorials below provide 
 tips and tricks on how to get started with Python."""

result = count_word_frequencies(python_article)
print(result)