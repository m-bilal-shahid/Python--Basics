# Membership Operators In Python
# Membership Operators Are Used To Test If A Value Or Variable Is Present In A Sequence (Like String, List, Tuple, etc.)

# Types Of Membership Operators:

# 1. in Operator:
#     Returns True if the specified value is present in the sequence
#     Returns False if it is not present

# 2. not in Operator:
#     Returns True if the specified value is NOT present in the sequence
#     Returns False if it is present


# Example Program:

word = input("Enter A Word: ")
char = input("Enter A Character To Search: ")

print("Character in Word:", char in word)         # True if char exists in word
print("Character not in Word:", char not in word) # True if char does not exist in word
