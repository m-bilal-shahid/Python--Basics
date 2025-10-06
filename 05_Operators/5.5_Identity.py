# Identity Operators In Python
# Identity Operators Are Used To Compare The Memory Location Of Two Objects (Not Their Values)
# They Check Whether Two Variables Refer To The Same Object In Memory

# Types Of Identity Operators:

# 1. is Operator:
#     Returns True if both variables refer to the same object (same memory address)
#     Returns False if they refer to different objects

# 2. is not Operator:
#     Returns True if both variables refer to different objects
#     Returns False if both refer to the same object


# Example Program:

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("a is b:", a is b)            # Checks if a and b refer to the same object
print("a is not b:", a is not b)    # Checks if a and b refer to different objects


