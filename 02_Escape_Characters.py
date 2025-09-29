# Python Basics - Topic 2: Escape Characters
'''
An escape sequence in Python is a special character combination that starts with a 
 backslash \ and gives a special meaning inside a string.

 They allow you to insert characters in a string that are normally hard or
  impossible to type (like newlines, tabs, quotes, etc.).
  '''

# 1: \n → New Line

# It Moves the cursor to the next line.
# Example:

print("Hello\nWorld")

# 2:  \t → Tab Space

# It Inserts a horizontal tab (like pressing the Tab key).
# Example:

print("Hello\tWorld")


# 3: \\ → Backslash

# It Displays a single backslash (\) in the output.
# Example:

print("This is a backslash: \\")


# 4: \'' → Single Quote

# It Allows you to use a single quote inside a string enclosed by single quotes.
# Example:

print('It\'s Python')


# 5: \" → Double Quote

# It Allows you to use double quotes inside a string enclosed by double quotes.
# Example:

print("He said, \"Python is easy\"")


# 6: \r → Carriage Return

# Definition: Moves the cursor back to the beginning of the line, 
# and the following text overwrites existing text.
# Example:

print("Hello\rWorld")



# 7: \b → Backspace

# It Deletes the character just before it.
# Example:

print("Hello\bWorld")