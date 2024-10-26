# Given two sets, write a function that determines if one set is a subset of the other. Do not use `<` or `>`

def is_subset(set1, set2):
    for elem in set1:
        if elem not in set2:
            return False
    return True

set1 = {1,2,3,4,5,6,7}
set2 = {7,8,9,10,11,12,13,14}

result = is_subset(set1, set2)
print(result)

set3 = {1,2,3,4,5,6,7}
set4 = {1,2,3,4,5,6,7,8}

result = is_subset(set3, set4)
print(result)