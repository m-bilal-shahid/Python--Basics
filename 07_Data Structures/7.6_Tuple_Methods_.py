# ---------------------------
# PYTHON TUPLE METHODS 
# ---------------------------

# NOTE:
# Tuples are IMMUTABLE (you cannot change elements),
# so they have only two built-in methods:
# → count()
# → index()
# But we can also use some common built-in functions with tuples.


# ---------------------------
# 1. count()
# ---------------------------

# Definition:
# Returns the number of times a specific value appears in the tuple.

t = (1, 2, 2, 3, 4, 2, 5)
result = t.count(2)
print("Count of 2:", result)

# Output: Count of 2: 3

# Roman Urdu Explanation:
# count() method tuple ke andar kisi value ki occurrence (kitni dafa aayi hai)
# uska number return karta hai.
# Upar example me "2" 3 dafa aayi hai, is liye output 3 aaya.


# ---------------------------
# 2. index()
# ---------------------------

# Definition:
# Returns the index (position) of the first occurrence of a value.

t = (10, 20, 30, 20, 40)
pos = t.index(20)
print("Index of 20:", pos)

# Output: Index of 20: 1



# Example with error handling:
# print(t.index(100))
# ❌ ValueError: tuple.index(x): x not in tuple
# Is liye ensure karo ke value tuple me exist karti ho.


# ---------------------------
# Other Built-in Functions Used with Tuples
# ---------------------------

# Even though tuples have few methods,
# Python’s built-in functions work perfectly with tuples.


# 3. len()
# Returns total number of elements in tuple
t = (5, 10, 15, 20)
print("Length:", len(t))
# Output: 4


# 4. max()
# Returns the largest element
t = (2, 5, 1, 9, 3)
print("Maximum:", max(t))
# Output: 9


# 5. min()
# Returns the smallest element
print("Minimum:", min(t))
# Output: 1


# 6. sum()
# Returns the sum of all numeric elements
t = (10, 20, 30)
print("Sum:", sum(t))
# Output: 60


# 7. sorted()
# Returns a sorted list (NOT tuple)
t = (4, 1, 3, 2)
print("Sorted:", sorted(t))
# Output: [1, 2, 3, 4]
# Roman Urdu:
# sorted() tuple ko sort karke ek nayi LIST return karta hai, tuple nahi.


# 8. any()
# Returns True if any element is True
t = (0, False, 5)
print("Any True?", any(t))
# Output: True


# 9. all()
# Returns True if all elements are True (non-zero)
t = (1, 2, 3)
print("All True?", all(t))
# Output: True


# 10. tuple() Constructor
# Converts other data types (like list, string) into a tuple
data = [1, 2, 3]
new_tuple = tuple(data)
print("Converted Tuple:", new_tuple)
# Output: (1, 2, 3)




