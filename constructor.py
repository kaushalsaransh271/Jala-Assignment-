#1. Class with default, one-argument & two-argument constructors
class Demo:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default Constructor")
        elif b is None:
            print("One Argument Constructor:", a)
        else:
            print("Two Argument Constructor:", a, b)


# Main class simulation
obj1 = Demo()
obj2 = Demo(10)
obj3 = Demo(10, 20)

#2. Call super class constructors from child class
class Parent:
    def __init__(self, x=None):
        if x is None:
            print("Parent Default Constructor")
        else:
            print("Parent Parameterized Constructor:", x)


class Child(Parent):
    def __init__(self):
        super().__init__()        # calling parent default constructor
        super().__init__(100)     # calling parent parameterized constructor
        print("Child Constructor")


# Main
c = Child()

#3. Apply access modifiers to constructors

class Sample:

    def __init__(self):
        print("Public Constructor")

    def _protected_constructor(self):
        print("Protected Constructor")

    def __private_constructor(self):
        print("Private Constructor")

    def access_private(self):
        self.__private_constructor()


obj = Sample()
obj._protected_constructor()     # allowed (but discouraged)
obj.access_private()             # correct way

#4. Program illustrating attributes of a constructor
class Student:
    def __init__(self, name, age):
        self.name = name      # attribute
        self.age = age        # attribute

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Main
s = Student("Saransh", 22)
s.display()
