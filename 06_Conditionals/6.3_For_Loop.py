'''For loop:

A for loop is used to repeat a block of code for each item in a sequence (numbers, strings, or ranges).

Think of it like this:

“For each item in a set, do this action.”

Syntax:

for variable in sequence:
    # code to run


variable → stores the current item of the sequence

sequence → can be a number range, string, or any iterable

The code block inside the loop runs for every item in the sequence'''

'''1: Example: Numbers using range()

Print numbers from 1 to 5:

for i in range(1, 6):  # 1 to 5 (6 is excluded)
    print(i)


Explanation:

range(1,6) generates numbers 1, 2, 3, 4, 5

i takes each number one by one

print(i) runs 5 times for each value
'''


'''2. Example: Numbers with step

Print even numbers from 2 to 10:

for i in range(2, 11, 2):  # start=2, stop=11, step=2
    print(i)


Explanation:
range(start, stop, step) → generates numbers starting from start, increasing by step, until just before stop
Here: 2, 4, 6, 8, 10


'''
'''3. Example: Iterating over a string

Print each character of "Python":

word = "Python"
for char in word:
    print(char)


Explanation:
A string is a sequence of characters
char takes each character one by one
Prints each letter on a new line
'''


'''4. Using break

Stop the loop when a condition is met:

for i in range(1, 10):
    if i == 5:
        break  # stops the loop completely
    print(i)


Explanation:

Loop starts from 1 to 9

When i becomes 5, break stops the loop immediately

Remaining numbers are not printed

'''

'''5. Using continue

Skip the current iteration:

for i in range(1, 6):
    if i == 3:
        continue  # skip this iteration
    print(i)


Explanation:

When i is 3, continue jumps to next iteration

3 is not printed, others are
'''

'''6. Using else with for

Code in else runs only if loop completes normally:

for i in range(1, 4):
    print(i)
else:
    print("Loop completed!")


Explanation:

Loop runs for 1,2,3

No break is used, so else executes after the loop'''



# Example 1:
# sum=0
# num=int(input("Enter A Number: "))
# print("All Numbers:")
# for i in range(1,num+1):
#     sum+=i
#     print(i)
    

# print("Even Numbers: ")
# for i in range (1,num+1):
#     if i%2==0:
#         print(i)

# print("Odd Numbers: ")
# for i in range (1,num+1):
#     if i%2!=0:
#         print(i)


# print("Sum:", sum)

# Example 2:

num = int(input("Enter A Number: "))

for i in range(1, num+1):
    if i > num/2:
        break
    if i % 7 == 0:
        continue
    print(i)
else:
    print("Loop Exited Without Break")



