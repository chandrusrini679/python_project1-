# 2.write a program to create the equation

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

Equation = (a + b + c) * (a - b - c) * a * b + a ** 2 + b ** 2 + (a * b * c) ** 3

print("the value of the equation is:", Equation)

# In this program, we first prompt the user to enter the values of a, b, and c. We then use these values to evaluate
# the equation (a+b+c) * (a-b-c) * ab + a^2 + b^2 + (abc)^3, and store the result in the variable equation. Finally,
# we print out the value of the equation using the print statement.
