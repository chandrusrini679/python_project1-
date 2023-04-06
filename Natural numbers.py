num = int(input("Enter the Natural Number: "))

if num % 2 == 0:
    print(num, "is even ")

else:
    print(num, "is odd")

# function is used to take user input for a natural number. The int() function is used to convert the input string to
# an integer.

# The number entered by the user is then checked to see if it is even or odd using the modulus operator %. If the
# remainder of the number divided by 2 is 0, then it is even; otherwise, it is odd.

# Finally, the program prints out a message indicating whether the number is even or odd.
# We define a class Point with x and y attributes, representing the x- and y-coordinates of a point in
# two-dimensional space.

# We define a function distance that takes two Point objects as arguments.

# The function calculates the distance between the two points using the formula sqrt((x1-x2)^2 + (y1-y2)^2).

# We use a try-except block to catch any AttributeErrors that may occur if the Point objects passed to the function
# do not have x and y attributes. In this case, the function returns an error message.

# If there are no errors, the function returns the calculated distance between the two points.
