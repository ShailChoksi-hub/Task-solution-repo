def is_palindrome(s):
    # checking for blank spaces and uneven characters
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("Output: true")
else:
    print("Output: false")
