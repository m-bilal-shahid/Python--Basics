# ---------------------------------------
# PYTHON SET 
# ---------------------------------------

# What is a Set?
# A set in Python is an unordered, unindexed collection of unique elements.
# - Unordered: No fixed position or index
# - No duplicates: All elements are unique
# - Mutable: You can add or remove elements
# - Heterogeneous: Can store different data types, but only immutable types

# Creating Sets
empty_set = set()                     # Empty set
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4}
mixed_set = {10, "Ali", True, 4.5}    # Different data types

# Duplicate values are removed automatically
example = {1, 2, 2, 3, 3, 3}          # Output: {1, 2, 3}

# Accessing Elements
# Sets do not support indexing like lists
# You can loop through elements
for item in fruits:
    print(item)



# Looping Through a Set
for x in fruits:
    print(x)

# Checking Membership
if "apple" in fruits:
    print("Apple found")

if "mango" not in fruits:
    print("Mango not found")

# Set Operations (Very Important)
# Union - Combines elements from both sets (without duplicates)
A = {1, 2, 3}
B = {3, 4, 5}
union_set = A | B                    # {1, 2, 3, 4, 5}

# Intersection - Common elements between sets
intersection_set = A & B             # {3}

# Difference - Elements in A but not in B
difference_set = A - B               # {1, 2}

# Symmetric Difference - Elements not common in both sets
symmetric_diff = A ^ B               # {1, 2, 4, 5}

# Set of Immutable Elements - Frozen Set
# A frozenset is like a set but it is immutable (cannot change after creation)
fs = frozenset([1, 2, 3, 4])
# fs.add(5)  # Error: 'frozenset' object has no attribute 'add'

# Important: Set cannot contain lists or dictionaries (because they are mutable)
# Valid example:
valid_set = {1, 2, (3, 4)}

# Invalid example (This causes an error):
# invalid_set = {1, 2, [3, 4]}   # Lists are mutable, cannot be added to set


