# Topic 7.1: Strings

'''1. Introduction:
A string in Python is a sequence of characters enclosed within quotes.
It can contain letters, numbers, symbols, or even spaces.

Python allows three types of quotes:

Single quotes ' '

Double quotes " "

Triple quotes ''' ''' or """ """

 Example:

name = "Bilal"
city = 'Lahore'
paragraph = """This is 
a multi-line 
string."""
'''




'''
2. Creating Strings

Strings can be created using single, double, or triple quotes.
Triple quotes are useful for multi-line strings or docstrings.

 Example:

single_quote = 'Hello'
double_quote = "World"
multi_line = """This is
a multi-line string."""


'''



'''
3. Accessing Characters (Indexing)

Each character in a string has a position number (called index).
Indexing starts from 0 for the first character.

 Example:

word = "Python"
print(word[0])   # First character
print(word[3])   # Fourth character
print(word[-1])  # Last character
'''


'''
4. String Slicing

Slicing extracts a portion (substring) of a string.

Syntax:

string[start:end:step]


start: index to begin from

end: index to stop (exclusive)

step (optional): difference between each index (default is 1)

Example:

name = "Bilal Ahmad"
print(name[0:5])     # From index 0 to 4
print(name[6:])      # From index 6 to end
print(name[:5])      # Same as name[0:5]
print(name[::2])     # Every 2nd character
print(name[::-1])    # Reverse the string
'''




'''

5.String Concatenation (Joining Strings)

You can join two or more strings using the + operator.

Example:

first = "Bilal"
last = "Ahmad"
full_name = first + " " + last
print(full_name)

'''

'''
6.String Repetition

You can repeat a string multiple times using the * operator.

 Example:

word = "Hi! "
print(word * 3)
'''



'''
7.String Length

The len() function returns the number of characters in a string (including spaces).

 Example:

text = "Python"
print(len(text))
'''

'''
8.Iterating Through a String

You can loop through a string using a for loop to process each character individually.

 Example:

for letter in "Python":
    print(letter)
'''


'''
9.String Immutability

Strings in Python are immutable, meaning once created, they cannot be changed directly.
You can create a new string instead.

 Wrong Example (Error):

word = "Hello"
word[0] = "Y"   # Error


 Correct Example:

word = "Hello"
new_word = "Y" + word[1:]
print(new_word)'''




