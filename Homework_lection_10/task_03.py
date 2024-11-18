def reverse_string(s):
    reversed_str = ""

    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]  
    return reversed_str

input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print(f"Reversed string: {reversed_string}")