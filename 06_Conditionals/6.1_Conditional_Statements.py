# Conditional Statements in Python

# Definition:
# Conditional statements allow your program to make decisions and execute certain blocks of code only if a condition is True.

# Basically, it’s like asking the program:
# "If this is true, do this; otherwise, do something else."

# Types of Conditional Statements in Python

'''1.if statement:

Executes a block of code if the condition is True.

Syntax:

if condition:
    # code to execute


Example:

age = 18
if age >= 18:
    print("You are an adult")'''


'''2.if-else statement

Executes one block if condition is True and another block if condition is False.

Syntax:

if condition:
    # code if True
else:
    # code if False


Example:

age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
'''

'''3. if-elif-else statement

Checks multiple conditions in order.

Syntax:

if condition1:
    # code1
elif condition2:
    # code2
else:
    # code if all conditions False


Example:

marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")'''



'''4. Nested if Statement in Python

Definition:
A nested if is an if statement inside another if statement.

Use it when you want to check a condition only if a previous condition is True.

Syntax
if condition1:
    # code if condition1 is True
    if condition2:
        # code if condition2 is also True
    else:
        # code if condition2 is False
else:
    # code if condition1 is False


Example:
age = 20
marks = 85

if age >= 18:
    print("You are an adult")
    if marks >= 80:
        print("You also scored very good marks!")
    else:
        print("Your marks are average.")
else:
    print("You are a minor")


Explanation:

First if checks whether age >= 18.

If True, it goes inside and checks marks >= 80.

If False, it prints "Your marks are average."

If age < 18, the outer else executes → "You are a minor".'''



# Example:

age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
marks = int(input("Enter Marks: "))


if age >= 18:
    if gender == 'Male':
        print("Adult Male")
    elif gender == 'Female':
        print("Adult Female")
    else:
        print("Invalid Gender")
else:
    print("Minor")


if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)


if marks >= 90 and age >= 18:
    print("Eligible for Scholarship")