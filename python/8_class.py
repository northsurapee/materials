# Create a class
class Person:
    # Class constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def hello(self):
        print("Hello my name is " + self.name)


# Create an object
p1 = Person("John", 36)

# Access object properties
print(p1.name)
print(p1.age)

# Call object method
p1.hello()
