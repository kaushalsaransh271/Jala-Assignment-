#1. Different ways of creating a string
s1 = "Hello"
s2 = 'World'
s3 = """This is
a multi-line
string"""

print(s1)
print(s2)
print(s3)

#2. Concatenating two strings using + operator

a = "Bright"
b = " IT Career"

result = a + b
print(result)

#3. Finding the length of the string
s = "Python"
print(len(s))

#4. Extract a string using Substring
s = "BrightITCareer"
sub = s[0:6]   # from index 0 to 5
print(sub)

#5. Searching in strings using index()
s = "Bright IT Career"
pos = s.index("IT")
print("Index:", pos)

#6. Matching a String Against a Regular Expression
import re

s = "Python123"
pattern = r"[A-Za-z0-9]+"

if re.fullmatch(pattern, s):
    print("Matched")
else:
    print("Not Matched")

#7. Comparing strings
a = "hello"
b = "hello"

if a == b:
    print("Strings are equal")
else:
    print("Strings are not equal")

#8. startsWith(), endsWith() and compareTo()
s = "BrightITCareer"

print(s.startswith("Bright"))
print(s.endswith("Career"))

# compareTo() equivalent
a = "apple"
b = "banana"

if a < b:
    print("a is smaller than b")
elif a > b:
    print("a is greater than b")
else:
    print("Both are equal")

#9. Trimming strings with strip()
s = "   Python   "
print(s.strip())

#10. Replacing characters in strings with replace()
s = "banana"
new_s = s.replace("a", "o")
print(new_s)

#11. Splitting strings with split()
s = "Python is easy"
words = s.split(" ")

print(words)

#12. Converting integer objects to Strings
num = 100
s = str(num)

print(s)
print(type(s))

#13. Converting to uppercase and lowercase
s = "Python"

print(s.upper())
print(s.lower())
