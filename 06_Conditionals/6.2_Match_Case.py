#  match-case Statement:
# Definition:

# The match-case statement in Python is a structural pattern matching feature introduced in Python 3.10. 
# It allows you to check a variable or expression against multiple values and execute a block of code corresponding to the matched value. 
# It is similar to switch-case statements in other languages like C/C++ or Java.

# match checks the variable or expression.

# case specifies the value to match against.

# _ is used as a default case (similar to else).

# Syntax:
# match variable:
#     case value1:
#         # code to execute if variable == value1
#     case value2:
#         # code to execute if variable == value2
#     case _:
#         # default block if no match

# Example 1: Simple Number Checker
num = int(input("Enter a number (1-3): "))

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid Number")

# Example 2: Color Checker 
color = input("Enter a color: ")

match color:
    case "red" | "Red" | "pink" | "Pink":
        print("Warm color")
    case "blue" | "Blue" | "green" | "Green":
        print("Cool color")
    case _:
        print("Unknown color")

# Example 3: Letter Checker 
letter = input("Enter a letter: ")

match letter:
    case 'a' | 'A':
        print("You entered A")
    case 'b' | 'B':
        print("You entered B")
    case _:
        print("Other letter")




