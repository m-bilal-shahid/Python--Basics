# Python Basics - Topic 3: Variables
'''
 A variable in Python is a name that is used to store a value in memory.
Think of it as a container/box with a label (name) that holds some data.

Example:

x = 10
name = "Bilal"


Here:

x is a variable storing the number 10

name is a variable storing the string "Bilal"

---  Rules for Naming Variables:
Rules for Naming Variables in Python

1. Start with a Letter or Underscore

    A variable name must begin with a letter (a–z, A–Z) or an underscore `_`.
    It cannot start with a number.

2. Use Only Letters, Numbers, and Underscores

    Variable names can contain letters, digits, and underscores.
    Spaces and special characters are not allowed.

3. Case Sensitive

    Variable names are case sensitive.
    `age`, `Age`, and `AGE` are considered three different variables.

4. Cannot Use Reserved Keywords

    Python keywords like `if`, `else`, `for`, `while`, `class`, `def`, etc., cannot be used as variable names.

5. Make Names Meaningful

    Variable names should describe the value or purpose of the variable clearly.

6. Use Underscore for Multiple Words (Optional)

    For multi-word variable names, use underscores to separate words (snake\_case).
'''


'''
---Variable Declaration and Assignment:

In Python, you don't need to declare the type. The type is automatically 
decided by the value you assign.

a = 5         # integer
b = 3.14      # float
c = "Hello"   # string
d = True      # boolean

--- Updating Variables:

You can change the value of a variable anytime.

x = 10
print(x)   # 10
x = 20
print(x)   # 20

--- Multiple Assignments:

Python allows assigning values in one line:

a, b, c = 1, 2, 3
print(a, b, c)   # 1 2 3

x = y = z = 100
print(x, y, z)   # 100 100 100

--- Dynamic Typing:

Python variables are dynamic, meaning the same variable can 
store different data types at different times.

x = 10
print(x)       # 10 (int)

x = "Python"
print(x)       # Python (string)

--- Types of Variables:

1: Global Variables → Defined outside functions, accessible everywhere.

2: Local Variables → Defined inside a function, accessible only in that function.

Example:

x = 50   # global variable

 def myFunc():     
    y = 10   # local variable
    print(y)

myFunc()  
print(x)'''


