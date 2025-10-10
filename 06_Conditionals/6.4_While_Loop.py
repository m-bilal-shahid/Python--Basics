'''Python while Loop
1. Definition

A while loop in Python is used to repeat a block of code as long as a condition is True.

It is called a pre-test loop because the condition is checked before executing the loop.

Useful when the number of iterations is not known beforehand.

2. Syntax
while condition:
    # code block to execute


condition → a boolean expression (True or False)

The loop continues to run as long as the condition is True

When the condition becomes False, the loop stops

3. Example 1: Simple while loop

Print numbers from 1 to 5:

i = 1
while i <= 5:
    print(i)
    i += 1  # increment i


Explanation:

Start with i = 1

Check condition i <= 5 → True → print i

Increment i by 1

Repeat until i > 5 → loop stops

4. Example 2: Using break

Stop the loop when a certain condition is met:

i = 1
while i <= 10:
    if i == 6:
        break  # stops the loop
    print(i)
    i += 1


Explanation:

Loop would normally run 1-10

When i == 6, break stops the loop immediately

5. Example 3: Using continue

Skip an iteration:

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # skip number 3
    print(i)


Explanation:

Increment i first

If i == 3, continue skips the print statement

Loop continues for remaining numbers

6. Example 4: Using else with while

The else block runs only if the loop terminates normally (condition becomes False, no break):

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed!")


Explanation:

Loop prints 1, 2, 3

No break is used → else runs

7. Key Points:

Use while when the number of iterations is unknown.

Infinite loops can happen if the condition never becomes False.

while True:
    print("Infinite loop")


break → stops the loop

continue → skips current iteration

else → executes if loop completes normally'''





# Example 1:
num = int(input("Enter A Positive Number: "))
i = 1

while i <= num:
    if i == 5:      
        i += 1      
        continue

    if i > num / 2:  
        break
    print(i)         
    i += 1







# # Example 2:
# num=int(input("Enter A Positive Number:"))
# sum=0
# i=1
# while(i<=num):
#     sum+=i
#     if sum>100:
#         break
#     i+=1

# else:
#    print("Loop Finished Without Sum Exceeding 100")

# print("Sum:", sum)