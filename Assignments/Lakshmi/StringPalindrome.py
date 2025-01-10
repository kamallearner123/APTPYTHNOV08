import string

def is_palindrome(input_string):
    # Remove spaces, punctuation, and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Check if cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]


# Example usage
input_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

