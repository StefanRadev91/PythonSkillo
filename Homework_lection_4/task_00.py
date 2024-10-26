def sum_elements(arr):
    result = 0
    for i in arr:
        result += i
    return result

# Test case 1
arr1 = [5, 6, 7, 8, 9, 10]
sum_arr1 = sum_elements(arr1)
print(sum_arr1)  

# Test case 2
arr2 = [1, 2, 3, 4, 5]
sum_arr2 = sum_elements(arr2)
print(sum_arr2)  

# Test case 3
arr3 = [-1, -2, -3, -4]
sum_arr3 = sum_elements(arr3)
print(sum_arr3)  

# Test case 4
arr4 = []
sum_arr4 = sum_elements(arr4)
print(sum_arr4)  

# Test case 5
arr5 = [0, 0, 0]
sum_arr5 = sum_elements(arr5)
print(sum_arr5)  