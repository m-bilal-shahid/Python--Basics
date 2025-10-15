# ---------------------------
# PYTHON LISTS - COMPLETE NOTES (A to Z)
# ---------------------------

# What is a List?
# A list in Python is a collection data type that is:
# - Ordered → items have a defined order and index
# - Mutable → items can be changed after creation
# - Allows duplicates → same value can appear multiple times
# - Heterogeneous → can store different data types in one list

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = [10, "Ali", True, 4.5]


# ---------------------------
# Creating Lists
# ---------------------------

# Empty list
my_list = []

# With elements
colors = ["red", "green", "blue"]

# Using list() constructor
letters = list(("a", "b", "c"))


# ---------------------------
# Accessing List Elements
# ---------------------------

# By Index
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   
print(fruits[-1])  

# By Slicing
print(fruits[0:2])   
print(fruits[:2])    
print(fruits[1:])    
print(fruits[::-1])  


# ---------------------------
# Updating List Elements
# ---------------------------

fruits[1] = "mango"
print(fruits)  


# ---------------------------
# Looping Through a List
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
    print("Yes, apple is in the list")

if "mango" not in fruits:
    print("No mango found")


# ---------------------------
# List Comprehension
# ---------------------------

# Basic Example
squares = [x**2 for x in range(5)]
print(squares)

# With Condition
even = [x for x in range(10) if x % 2 == 0]
print(even)

# Nested Comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)


# ---------------------------
# Copying Lists (Important Concept)
# ---------------------------

# Assignment (Reference)
a = [1, 2, 3]
b = a
a[0] = 100
print(b)

# Copy (New Object)
a = [1, 2, 3]
b = a.copy()
a[0] = 100
print(b)


# ---------------------------
# Nested Lists
# ---------------------------

# A list inside another list.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])
print(matrix[1][2])


# ---------------------------
# Combining and Repeating Lists
# ---------------------------

list1 = [1, 2, 3]
list2 = [4, 5]

# Concatenation
combined = list1 + list2  

# Repetition
repeat = list1 * 2        


# ---------------------------
# Comparing Lists
# ---------------------------

# Lists are compared element by element.
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   
print(a is b)   


# ---------------------------
# Converting Other Data Types to List
# ---------------------------

string = "Python"
chars = list(string)
print(chars)

tuple_data = (1, 2, 3)
list_data = list(tuple_data)


# ---------------------------
# Enumerate Function (Advanced)
# ---------------------------

# Used to loop through list with both index and value.
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)


# ---------------------------
# List Unpacking
# ---------------------------

# Unpack list elements into variables.
fruits = ["apple", "banana", "cherry"]
a, b, c = fruits
print(a)
print(b)
print(c)

# Using * for multiple
numbers = [10, 20, 30, 40, 50]
a, *b, c = numbers
print(a)
print(b)
print(c)
