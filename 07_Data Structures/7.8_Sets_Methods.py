# -------------------------------------------------------
# PYTHON SET METHODS
# -------------------------------------------------------

# Sample Set for Methods
fruits = {"apple", "banana", "cherry"}

# 1. add()
# Adds a single element to the set
fruits.add("mango")

# 2. update()
# Adds multiple elements (from list, tuple, set, etc.)
fruits.update(["orange", "grapes"])

# 3. remove()
# Removes specified element
# Raises error if element does not exist
fruits.remove("banana")

# 4. discard()
# Removes specified element
# Does not raise error if element not found
fruits.discard("banana")

# 5. pop()
# Removes and returns a random element from the set
item = fruits.pop()

# 6. clear()
# Removes all elements from the set
fruits.clear()

# 7. copy()
# Returns a shallow copy of the set
A = {1, 2, 3}
B = A.copy()

# ---------------------------------------
# Set Operations (also as methods)
# ---------------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 8. union()
# Returns all unique elements from both sets
C = A.union(B)         # {1, 2, 3, 4, 5, 6}
# OR: C = A | B

# 9. intersection()
# Returns common elements
D = A.intersection(B)  # {3, 4}
# OR: D = A & B

# 10. difference()
# Elements in A but not in B
E = A.difference(B)    # {1, 2}
# OR: E = A - B

# 11. symmetric_difference()
# Elements not common in both sets
F = A.symmetric_difference(B)  # {1, 2, 5, 6}
# OR: F = A ^ B

# ---------------------------------------
# Relationship Testing Methods
# ---------------------------------------

# 12. issubset()
# Checks if all elements of A are in B
subset_check = {1, 2}.issubset(A)      # True

# 13. issuperset()
# Checks if A contains all elements of B
superset_check = A.issuperset({1, 2})  # True

# 14. isdisjoint()
# Returns True if sets have no common elements
G = {7, 8}
disjoint_check = A.isdisjoint(G)       # True


