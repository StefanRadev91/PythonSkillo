# Write a function to remove duplicates from a list using a set.

def removing_duplicates(test_list):
    my_set = set()
    for element in test_list:
        my_set.add(element)
    return my_set
my_list = ["Arsenal", "Manchester United", "Arsenal", "Chelsea", "Chelsea", "Manchester United"]

result = removing_duplicates(my_list)
print(result)

def removing_duplicates2(test_list):
    return set(test_list)

result = removing_duplicates2(my_list)
print(result)

