from .class1 import ClassOne
from .class2 import ClassTwo


class ClassOne:
    def __init__(self, name):
        self.name = name   # constructor initializes name

    def greet(self):
        return f"Hello from ClassOne, {self.name}!"

class ClassTwo:
    def __init__(self, age):
        self.age = age   # constructor initializes age

    def show_age(self):
        return f"ClassTwo says: Age is {self.age}"
        
        
# Import classes from the package
from My_Package import ClassOne, ClassTwo

def main():
    # Create objects
    obj1 = ClassOne("Alice")
    obj2 = ClassTwo(25)

    # Call methods
    print(obj1.greet())
    print(obj2.show_age())

if __name__ == "__main__":
    main()
