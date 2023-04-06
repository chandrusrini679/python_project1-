x = " 89e9jcd^o38829@3%3,/mkl$w1"

number_only = ''.join(filter(str.isdigit, x))

print(number_only)

# This code uses the filter() function to create an iterator
# that only includes the numeric characters in the string
# x. The str.isdigit() method is used as the filtering function
# to check if each character is a digit.

# Then we use the join() method to concatenate the filtered iterator back into a single string. The resulting string
# numbers_only contains only the numeric characters from the original string x.
