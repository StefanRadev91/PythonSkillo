with open("/Users/stefanradev/Documents/SkilloPython/Homework_lection_9/words.txt", "r") as file:
    lines = file.readlines()

word_count = 0

for line in lines:
    words = line.strip().split()  
    word_count += len(words)  

print(f"The total number of words in 'words.txt' is: {word_count}")