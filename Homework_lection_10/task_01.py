def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("Enter a word or phrase: ")

if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")