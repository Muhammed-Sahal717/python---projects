# inheritance example

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

dog1 = Dog("Charlie")
cat1 = Cat("Buddy")

dog1.speak()  # outputs "Charlie barks."
cat1.speak()  # outputs "Buddy meows."


# multiple inheritance example
class Flyer:
    def fly(self):
        print("I can fly!")

class Bird(Animal, Flyer):
    def __init__(self, name):
        super().__init__(name)

bird1 = Bird("Tweety")
bird1.speak()  # outputs "Tweety makes a sound."
bird1.fly()    # outputs "I can fly!"


# Multi-level inheritance example
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")


# inheritance means use the properties and methods of the parent class in the child class