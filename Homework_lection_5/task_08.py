def hash_list(input_list):
    list_tuple = tuple(input_list)
    return hash(list_tuple)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [1, 2, 3]  

print(f"Hash of list1: {hash_list(list1)}")
print(f"Hash of list2: {hash_list(list2)}")
print(f"Hash of list3: {hash_list(list3)}")  