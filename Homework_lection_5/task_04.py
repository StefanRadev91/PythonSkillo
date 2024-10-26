# Write a function that takes a list and returns the sum of all even numbers in the list.

def all_even_numbers_in_a_list(list):
    sum_of_even_numbers = 0
    for i in list:
        if i % 2 == 0:
            sum_of_even_numbers+=i
    return sum_of_even_numbers

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]

result = all_even_numbers_in_a_list(list_of_numbers)

print(result)
