# 1. Write a function for arithmetic operators (+, −, , /)
def arithmetic(a, b):
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)
    print("Division =", a / b)

arithmetic(20, 10)

#2. Write a method for increment and decrement operators (++, --)
def increment_decrement(num):
    num = num + 1
    print("After Increment =", num)

    num = num - 1
    print("After Decrement =", num)

increment_decrement(5)

#3. Write a program to find the two numbers equal or not
a = 10
b = 10

if a == b:
    print("Both numbers are equal")
else:
    print("Numbers are not equal")

#4. Program for relational operators (<, <=, >, >=)
a = 10
b = 20

print("a < b =", a < b)
print("a <= b =", a <= b)
print("a > b =", a > b)
print("a >= b =", a >= b)

#5. Print the smaller and larger number
a = 25
b = 15

if a > b:
    print("Larger number =", a)
    print("Smaller number =", b)
else:
    print("Larger number =", b)
    print("Smaller number =", a)
