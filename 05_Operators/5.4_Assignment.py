# Assignment Operators in Python
# Assignment operators are used to assign values to variables.

# 1. =  (Simple Assignment)
# Assigns the value on right to the variable on left
a = 10
print("a =", a)

# 2. +=  (Add AND Assign)
# Adds right value to left variable and assigns the result
a += 5     # a = a + 5
print("a += 5 →", a)

# 3. -=  (Subtract AND Assign)
# Subtracts right value from left variable and assigns the result
a -= 3     # a = a - 3
print("a -= 3 →", a)

# 4. *=  (Multiply AND Assign)
# Multiplies and assigns the result
a *= 2     # a = a * 2
print("a *= 2 →", a)

# 5. /=  (Divide AND Assign)
# Divides and assigns the result (result is float)
a /= 2     # a = a / 2
print("a /= 2 →", a)

# 6. //=  (Floor Divide AND Assign)
# Floor divide and assign (integer part only)
a //= 2    # a = a // 2
print("a //= 2 →", a)

# 7. %=  (Modulus AND Assign)
# Takes remainder and assigns it back
a %= 3     # a = a % 3
print("a %= 3 →", a)

# 8. **=  (Exponent AND Assign)
# Raises variable to the power and assigns back
a **= 2    # a = a ** 2
print("a **= 2 →", a)






#  Example Program

# Taking Input from User
a = int(input("Enter a Number: "))

print("\nOriginal Value of a:", a)

# 1. Simple Assignment (=)
b = a
print("Simple Assignment (=):", b)

# 2. Add and Assign (+=)
a += 5
print("After a += 5:", a)

# 3. Subtract and Assign (-=)
a -= 2
print("After a -= 2:", a)

# 4. Multiply and Assign (*=)
a *= 3
print("After a *= 3:", a)

# 5. Divide and Assign (/=)
a /= 2
print("After a /= 2:", a)

# 6. Floor Divide and Assign (//=)
a //= 2
print("After a //= 2:", a)

# 7. Modulus and Assign (%=)
a %= 4
print("After a %= 4:", a)

# 8. Exponent and Assign (**=)
a **= 2
print("After a **= 2:", a)
