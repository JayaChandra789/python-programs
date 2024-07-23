#Program using constructors with [class,def]keywords
class Person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"Name : {self.name},Age : {self.age}")

person1=Person("jaya",21)
person1.display_info()


'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an instance of the Person class
person1 = Person("Alice", 30)
person1.display_info()  # Output: Name: Alice, Age: 30

# Creating another instance of the Person class
person2 = Person("Bob", 25)
person2.display_info()  # Output: Name: Bob, Age: 25 '''

