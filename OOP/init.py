class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

person1 = Person("sahal", 20)
person1.introduce()
# we can call in one line as well
Person("sahal", 20).introduce()


# example for default constructor
class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

car1 = Car()
car1.display_info()