# Python Basics - Topic 4: Data Types & Input


# 1. What are Data Types?
# -------------------------------
# In Python, data types tell us what kind of value
# is stored inside a variable.
# Example: age = 25 (here 25 is an integer data type)
# Python is dynamically typed -> we don’t need to declare type manually.

# -------------------------------
# 2. Basic Data Types with Examples
# -------------------------------

# Integer (int): Whole numbers (positive or negative)
age = 25
print("Age:", age, "| Type:", type(age))  # <class 'int'>

# Float: Numbers with decimals
height = 5.9
print("Height:", height, "| Type:", type(height))  # <class 'float'>

# String (str): Sequence of characters (text data)
name = "Ali"
print("Name:", name, "| Type:", type(name))  # <class 'str'>

# Boolean (bool): Logical values -> True / False
is_student = True
print("Is Student:", is_student, "| Type:", type(is_student))  # <class 'bool'>

# Complex: Numbers with real and imaginary parts
z = 3 + 4j
print("Complex Number:", z, "| Type:", type(z))  # <class 'complex'>

# -------------------------------
# 3. type() Function
# -------------------------------
# type() function is used to check the data type of any variable.

print("\n--- Checking Data Types Using type() Function ---")
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))
print("Type of z:", type(z))

# -------------------------------
# 4. Type Casting (Type Conversion)
# -------------------------------
# Sometimes we need to change a variable’s type.
# This is called Type Casting.
# Python provides built-in functions for this:
# int(), float(), str(), bool()

x = "100"  # String type
print("\nOriginal x:", x, "| Type:", type(x))

# Convert String to Integer
y = int(x)
print("After int(x):", y, "| Type:", type(y))

# Convert String to Float
z_float = float(x)
print("After float(x):", z_float, "| Type:", type(z_float))

# Convert Integer to String
num_str = str(y)
print("After str(y):", num_str, "| Type:", type(num_str))

# Convert Integer to Boolean
# Rule: 0 -> False, Any non-zero -> True
bool_val = bool(y)
print("After bool(y):", bool_val, "| Type:", type(bool_val))

# -------------------------------
# 5. Input in Python
# -------------------------------
# input() function is used to take input from the user.
# IMPORTANT: By default, input() always returns a string.

print("\n--- Input Examples ---")

# Example 1: Taking String Input
user_name = input("Enter your name: ")
print("Hello,", user_name, "| Type:", type(user_name))

# Example 2: Taking Integer Input
user_age = int(input("Enter your age: "))  # converting str -> int
print("Your Age:", user_age, "| Type:", type(user_age))

# Example 3: Taking Float Input
user_height = float(input("Enter your height in meters: "))
print("Your Height:", user_height, "| Type:", type(user_height))

# Example 4: Taking Boolean Input
# Trick: First take input as int (0 or 1), then convert to bool
is_student_input = bool(int(input("Are you a student? (1 for Yes, 0 for No): ")))
print("Is Student:", is_student_input, "| Type:", type(is_student_input))


# -------------------------------
# 6. Example Program
# -------------------------------




# Taking different inputs
name = input("Enter your full name: ")             # string
age = int(input("Enter your age: "))               # integer
height = float(input("Enter your height (in meters): "))  # float
marks = float(input("Enter your marks (out of 100): "))   # float
is_student = bool(int(input("Are you currently a student? (1 for Yes, 0 for No): ")))

# Doing some operations
future_age = age + 5  # int calculation
percentage = (marks / 100) * 100  # float calculation
height_in_cm = int(height * 100)  # float -> int conversion

# Displaying results
print("\n--- User Profile ---")
print("Name:", name, "| Type:", type(name))
print("Age (Now):", age, "| Type:", type(age))
print("Age (After 5 years):", future_age)
print("Height:", height, "meters |", height_in_cm, "cm")
print("Marks:", marks, "| Percentage:", percentage, "%")
print("Student Status:", is_student, "| Type:", type(is_student))