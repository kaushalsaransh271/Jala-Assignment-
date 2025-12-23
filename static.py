#1. Define a static variable and access that through a class
class Student:
    college = "ABC College"   # static (class) variable

print(Student.college)

# 2. Define a static variable and access that through an instance
class Student:
    college = "ABC College"   # static variable

s1 = Student()
print(s1.college)

#3. Define a static variable and change within the instance
class Student:
    college = "ABC College"

s1 = Student()
s1.college = "XYZ College"

print("Instance value:", s1.college)
print("Class value:", Student.college)

#4. Define a static variable and change within the class
class Student:
    college = "ABC College"

Student.college = "XYZ College"

s1 = Student()
s2 = Student()

print(s1.college)
print(s2.college)
