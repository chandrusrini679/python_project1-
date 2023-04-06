import math


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    try:
        dist = math.sqrt((p1.x, p2.y) ** 2 + (p1.x - p2.y) ** 2)
        return dist
    except AttributeError:
        return "Error: INVALID INPUT.please provide point with x and y"


# create two Point objects
p1 = point(1, 2)
p2 = point(4, 6)

# calculate the distance between the two points
dist = distance(p1, p2)

# print the result
print(dist)  # output: 5.0

# We define a class Point with x and y attributes, representing the x- and y-coordinates of a point in
# two-dimensional space.

# We define a function distance that takes two Point objects as arguments.

# The function calculates the distance between the two points using the formula sqrt((x1-x2)^2 + (y1-y2)^2).

# We use a try-except block to catch any AttributeErrors that may occur if the Point objects passed to the function
# do not have x and y attributes. In this case, the function returns an error message.

# If there are no errors, the function returns the calculated distance between the two points.



