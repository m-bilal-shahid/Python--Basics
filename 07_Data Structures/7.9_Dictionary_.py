# --------------------------------------------------------
# PYTHON DICTIONARY 
# --------------------------------------------------------

# What is a Dictionary?
# A dictionary in Python is an unordered, mutable collection of key-value pairs.
# - Each value is accessed using its key (not index)
# It is just like the real dictionary
# - Keys must be unique and immutable (string, number, tuple)
# - Values can be of any data type
# - Syntax: {key: value}

# Creating Dictionaries
empty_dict = {}
student = {"name": "Bilal", "age": 21, "course": "AI"}

# Using dict() constructor
info = dict(name="Ali", age=22, country="Pakistan")

# Dictionary with mixed data types
data = {
    "name": "Ahmad",
    "marks": [85, 90, 88],
    "passed": True,
    "details": {"city": "Lahore", "semester": 3}
}

# Accessing Values
print(student["name"])      # Access using key
print(student.get("age"))   # get() avoids error if key does not exist

# Adding New Key-Value Pair
student["grade"] = "A"

# Updating Existing Value
student["age"] = 22

# Nested Dictionary Access
print(data["details"]["city"])

# Dictionary Length
print(len(student))

# Keys Must Be Unique – Last value is stored
sample = {
    "a": 1,
    "b": 2,
    "a": 5
}
# Result: {"a": 5, "b": 2}

# Looping Through Dictionary
for key in student:
    print(key)          # keys

for key in student:
    print(student[key]) # values using key

for key, value in student.items():
    print(key, value)   # both key and value

# Checking Membership (Only checks keys, not values)
if "name" in student:
    print("Found")

if "Ali" not in student:
    print("Not Found")

# Copying Dictionary (Avoid Reference Issue)
dict1 = {"a": 1, "b": 2}
dict2 = dict1.copy()       # Creates a new dictionary (shallow copy)



# Dictionary from List of Keys
keys = ["a", "b", "c"]
default_value = 0
result = dict.fromkeys(keys, default_value)

# Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
# Result: {1:1, 2:4, 3:9, 4:16, 5:25}

