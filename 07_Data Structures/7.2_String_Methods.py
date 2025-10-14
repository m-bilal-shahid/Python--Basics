# Topic 7.2: String Methods



#  1. upper()

# Definition: Converts all characters in a string to uppercase (capital letters).
# Example:

text = "hello"
print(text.upper())   # Output: HELLO

#  2. lower()

# Definition: Converts all characters in a string to lowercase (small letters).
# Example:

text = "HELLO"
print(text.lower())   # Output: hello

#  3. capitalize()

# Definition: Converts only the first character of the string to uppercase and the rest to lowercase.
# Example:

text = "python is fun"
print(text.capitalize())   # Output: Python is fun

#  4. title()

# Definition: Converts the first character of each word to uppercase.
# Example:

text = "hello world"
print(text.title())   # Output: Hello World

#  5. swapcase()

# Definition: Converts uppercase letters to lowercase and lowercase letters to uppercase.
# Example:

text = "HeLLo"
print(text.swapcase())   # Output: hEllO

#  6. split()

# Definition: Splits a string into a list using whitespace or a specified separator.
# Example:

text = "apple,banana,grape"
print(text.split(','))   # Output: ['apple', 'banana', 'grape']

#  7. join()

# Definition: Joins list items into a single string using a separator.
# Example:

items = ['a', 'b', 'c']
print('-'.join(items))   # Output: a-b-c

#  8. replace()

# Definition: Replaces one substring with another.
# Example:

text = "I like Java"
print(text.replace("Java", "Python"))   # Output: I like Python

#  9. format()

# Definition: Formats strings by inserting values into placeholders {}.
# Example:

name = "Alice"
age = 20
print("My name is {} and I am {} years old".format(name, age))
# Output: My name is Alice and I am 20 years old

#  10. find()

# Definition: Returns the index of the first occurrence of a substring, or -1 if not found.
# Example:

text = "banana"
print(text.find("a"))   # Output: 1

#  11. count()

# Definition: Returns how many times a substring appears in the string.
# Example:

text = "banana"
print(text.count("a"))   # Output: 3

#  12. startswith()

# Definition: Checks if a string starts with the specified prefix. Returns True or False.
# Example:

text = "hello world"
print(text.startswith("hello"))   # Output: True

#  13. endswith()

# Definition: Checks if a string ends with the specified suffix. Returns True or False.
# Example:

text = "file.txt"
print(text.endswith(".txt"))   # Output: True

#  14. strip()

# Definition: Removes leading and trailing spaces (or specified characters).
# Example:

text = "---hello---"
print(text.strip('-'))   # Output: hello

#  15. lstrip()

# Definition: Removes spaces or specified characters from the left side.
# Example:

text = "   hello"
print(text.lstrip())   # Output: hello

#  16. rstrip()

# Definition: Removes spaces or specified characters from the right side.
# Example:

text = "hello   "
print(text.rstrip())   # Output: hello

#  17. isalnum()

# Definition: Returns True if all characters are alphanumeric (letters and numbers only).
# Example:

text = "abc123"
print(text.isalnum())   # Output: True

#  18. isalpha()

# Definition: Returns True if all characters are alphabetic (letters only).
# Example:

text = "Python"
print(text.isalpha())   # Output: True

#  19. isdigit()

# Definition: Returns True if all characters are digits (0–9).
# Example:

text = "12345"
print(text.isdigit())   # Output: True

#  20. islower() / isupper()

# Definition:

# islower() → Returns True if all characters are lowercase.

# isupper() → Returns True if all characters are uppercase.
# Example:

a = "hello"
b = "HELLO"
print(a.islower())   # Output: True
print(b.isupper())   # Output: True