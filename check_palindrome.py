my_string = "abcba"

if my_string == my_string[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# Output
# palindrome
# another way


def palindrome(string):
    return string == string[::-1]


palindrome('python')  # False
