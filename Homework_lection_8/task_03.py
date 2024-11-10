# Problem 2:
# Research and understand how does selections sort work.
# Debug and fix the following code to make it correct
# def selection_sort(arr):
# for i in range(len(arr)):
# min_index = i
# for j in range(i + 1, len(arr)):
# if arr[i] < arr[min_index]:
# min_index = j
# arr[i], arr[min_index] = arr[min_index], arr[i]
# return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        print(f"Step {i+1}: Начална подредба: {arr}") 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
            print(f"  Сравнение на елементите: arr[{j}] = {arr[j]} с arr[{min_index}] = {arr[min_index]}")
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"  Размяна: arr[{i}] с arr[{min_index}], нова подредба: {arr}")
    print(f"Подреден масив: {arr}")
    return arr

arr = [7, 3, 23, 17, 77]
sorted_arr = selection_sort(arr)