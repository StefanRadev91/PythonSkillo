tuple_of_integers = (1, 2, 3, 4, 5, 6, 6, 7, 8, 10, 22, 199, 33, 21, 40, 50, 200, 44)

max_number = tuple_of_integers[0]
min_number = tuple_of_integers[0]

for i in tuple_of_integers:
    if i > max_number:
        max_number = i
    if i < min_number:
        min_number = i

print("Maximum value:", max_number)
print("Minimum value:", min_number)
