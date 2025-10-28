# --------------------------------------------------------
# PYTHON DICTIONARY METHODS 
# --------------------------------------------------------

student = {"name": "Bilal", "age": 21, "course": "AI"}

# 1. keys()
# Returns all keys of the dictionary
student.keys()

# 2. values()
# Returns all values of the dictionary
student.values()

# 3. items()
# Returns key-value pairs as tuples
student.items()

# 4. get(key, default_value)
# Returns value of key; returns default_value if key not found
student.get("name")
student.get("grade", "Not Found")

# 5. update()
# Adds new key-value pair or updates existing key's value
student.update({"grade": "A", "age": 22})

# 6. pop(key)
# Removes key and returns its value
student.pop("age")

# 7. popitem()
# Removes and returns the last inserted key-value pair
student.popitem()

# 8. del
# Deletes a specific key or entire dictionary
# del student["name"]
# del student

# 9. clear()
# Removes all key-value pairs
student.clear()

# 10. copy()
# Returns shallow copy of the dictionary
original = {"a": 1, "b": 2}
duplicate = original.copy()

# 11. fromkeys()
# Creates dictionary with given keys, same default value for all
keys = ["x", "y", "z"]
new_dict = dict.fromkeys(keys, 0)

# 12. setdefault(key, default_value)
# Returns value of key; if key not found, adds key with default_value
car = {"brand": "Toyota", "year": 2022}
car.setdefault("color", "Black")  # Adds color if absent




