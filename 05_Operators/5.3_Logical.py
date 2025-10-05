# Logical Operators in Python
# Logical operators are used to combine conditional statements.
# They return True or False based on logic.

# 1. and :
# Returns True if BOTH conditions are True.
print(5 > 3 and 10 > 2)   # True (both True)
print(5 > 3 and 2 > 10)   # False (one False)

# 2. or :
# Returns True if ANY ONE condition is True.
print(5 > 3 or 2 > 10)    # True (one True)
print(2 > 10 or 1 > 5)    # False (both False)

# 3. not :
# Reverses the result — True becomes False, False becomes True.
print(not(5 > 3))         # False (because 5 > 3 is True)
print(not(2 > 10))        # True (because 2 > 10 is False)


# Example with user input:
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)
print("not(a > b):", not(a > b))
