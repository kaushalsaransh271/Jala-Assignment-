#1. Print “Bright IT Career” ten times using for loop
for i in range(10):
    print("Bright IT Career")

#2. Print 1 to 20 numbers using while loop
num = 1
while num <= 20:
    print(num)
    num += 1

# 3. Program for equal and not equal operators
a = 10
b = 10

if a == b:
    print("Both numbers are equal")
else:
    print("Numbers are not equal")

#4. Print odd and even numbers
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

#5. Print largest number among three numbers
a = 10
b = 25
c = 15

if a > b and a > c:
    print("Largest =", a)
elif b > c:
    print("Largest =", b)
else:
    print("Largest =", c)

#6. Print even numbers between 10 and 20 using while
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1
#7. Print 1 to 10 using do-while loop
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break
#8. Armstrong number
num = 153
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit * digit * digit
    num = num // 10

if temp == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong")

#9. Prime number
num = 7
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime")

#10. Palindrome number
num = 121
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#11. EVEN or ODD using switch
num = 10

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#12. Print gender (Male/Female) using M/F

gender = 'M'

if gender == 'M':
    print("Male")
elif gender == 'F':
    print("Female")
else:
    print("Invalid input")
