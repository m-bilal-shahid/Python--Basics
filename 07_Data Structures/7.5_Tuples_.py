# ---------------------------
# PYTHON TUPLES 
# ---------------------------

# What is a Tuple?
# A tuple in Python is a collection data type that is:
# - Ordered → items have a defined order and index
# - Immutable → items cannot be changed after creation
# - Allows duplicates → same value can appear multiple times
# - Heterogeneous → can store different data types in one tuple

fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4)
mixed = (10, "Ali", True, 4.5)


# ---------------------------
# Creating Tuples
# ---------------------------

# Empty tuple
my_tuple = ()

# With elements
colors = ("red", "green", "blue")

# Using tuple() constructor
letters = tuple(("a", "b", "c"))

# Single element tuple (Note the comma!)
single = ("apple",)
not_tuple = ("apple")  # This is a string


# ---------------------------
# Accessing Tuple Elements
# ---------------------------

fruits = ("apple", "banana", "cherry")

# By Index
print(fruits[0])      # first element
print(fruits[-1])     # last element

# By Slicing
print(fruits[0:2])    # elements from index 0 to 1
print(fruits[:2])     
print(fruits[1:])     
print(fruits[::-1])   # reverse tuple


# ---------------------------
# Looping Through a Tuple
# ---------------------------

# Using for-loop
for fruit in fruits:
    print(fruit)

# Using index
for i in range(len(fruits)):
    print(i, fruits[i])


# ---------------------------
# Membership Operators
# ---------------------------

if "apple" in fruits:
    print("Yes, apple is in the tuple")

if "mango" not in fruits:
    print("No mango found")


# ---------------------------
# Tuple Immutability 
# ---------------------------

# Tuples cannot be changed directly.
# Example:
numbers = (10, 20, 30)
# numbers[0] = 100  ❌ This will cause an error

# To modify, convert to list, then back to tuple:
temp = list(numbers)
temp[0] = 100
numbers = tuple(temp)
print(numbers)


# ---------------------------
# Nested Tuples
# ---------------------------

# A tuple inside another tuple
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(matrix[0])
print(matrix[1][2])


# ---------------------------
# Combining and Repeating Tuples
# ---------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5)

# Concatenation
combined = tuple1 + tuple2
print(combined)

# Repetition
repeat = tuple1 * 2
print(repeat)


# ---------------------------
# Comparing Tuples
# ---------------------------

# Tuples are compared element by element.
a = (1, 2, 3)
b = (1, 2, 3)
print(a == b)   # True
print(a is b)   # False (different memory locations)


# ---------------------------
# Tuple Packing and Unpacking
# ---------------------------

# Packing
person = ("Ali", 21, "Lahore")

# Unpacking
name, age, city = person
print(name)
print(age)
print(city)

# Using * for multiple unpacking
numbers = (10, 20, 30, 40, 50)
a, *b, c = numbers
print(a)
print(b)
print(c)




# ---------------------------
# Converting Other Data Types to Tuple
# ---------------------------

# From list
list_data = [1, 2, 3]
tuple_data = tuple(list_data)
print(tuple_data)

# From string
string = "Python"
chars = tuple(string)
print(chars)


# ---------------------------
# Enumerate Function with Tuples
# ---------------------------

fruits = ("apple", "banana", "cherry")
for index, value in enumerate(fruits):
    print(index, value)

