# Ternary Operator In Python
# Ternary Operator Is A Short Way Of Writing If-Else Statement In One Line

#  Syntax:
# variable = value_if_true if condition else value_if_false

#  Meaning:
# If condition is True → value_if_true assigned
# Else → value_if_false assigned

#  It Is Also Called Conditional Expression
# Useful For Simple If-Else Conditions In One Line

# Example 1:
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

# Find The Greater Number Using Ternary Operator
greater = a if a > b else b
print("Greater Number Is:", greater)

# Example 2:
num = int(input("Enter A Number: "))

# Check Even Or Odd Using Ternary Operator
result = "Even" if num % 2 == 0 else "Odd"
print("The Number Is:", result)
