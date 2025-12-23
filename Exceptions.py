#1. Generate Arithmetic Exception (without handling)
a = 10
b = 0
print(a / b)   # ZeroDivisionError

#2. Handle Arithmetic Exception using try–except
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Arithmetic Exception: Division by zero")

#3. Method which throws exception, call without try block
def divide():
    return 10 / 0   # exception thrown

divide()   # no try block

#4. Program with multiple catch blocks
try:
    x = int("abc")
    y = 10 / 0
except ValueError:
    print("ValueError occurred")
except ZeroDivisionError:
    print("ZeroDivisionError occurred")

#5. Throw exception with your own message
age = 15

if age < 18:
    raise Exception("Age must be 18 or above")

#6. Create your own exception
class MyException(Exception):
    pass

raise MyException("This is my custom exception")

#7. Program with finally block
try:
    a = 10 / 2
    print(a)
except ZeroDivisionError:
    print("Error")
finally:
    print("Finally block executed")

#8. Generate Arithmetic Exception
num = 5
print(num / 0)

#9. Generate FileNotFoundException (Python equivalent)
file = open("no_file.txt", "r")

#10. Generate ClassNotFoundException (Python equivalent)
import non_existing_module

#11. Generate IOException (Python equivalent)
file = open("/root/secret_file.txt", "r")

#12. Generate NoSuchFieldException (Python equivalent)
class Sample:
    def __init__(self):
        self.value = 10

