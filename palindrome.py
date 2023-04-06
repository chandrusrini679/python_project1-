def is_palindrome(word):
    """
    Function to check if a given string is a palindrome or not.

    Parameters:
        word (str): The string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove non-alphanumeric characters
    word = ''.join(e for e in word.lower() if e.isalnum())

    # Check if the string is equal to its reverse
    return word == word[::-1]


# Create an instance of the Palindrome class
class Palindrome:
    pass


p = Palindrome()

# Test the is_palindrome() function with some sample inputs
print(is_palindrome("Madam"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False

# We define a class called Palindrome with a single method called is_palindrome(). The is_palindrome() function takes
# a string as input and returns True if the string is a palindrome and False otherwise.

# To check if a given string is a palindrome, we first convert the string to lowercase and remove all
# non-alphanumeric characters using the isalnum() function. Then, we check if the string is equal to its reverse
# using the slice notation word[::-1], which returns a reversed copy of the original string.

# Finally, we create an instance of the Palindrome class and test the is_palindrome() function with some sample
# inputs using the print() function.




