1. Define what Object Oriented Programming is in your own words
OOP is a way of writing code where we create "objects" to represent real-world things. These objects are built using "classes" that define the properties and behaviors the objects will have. It helps organize code so it's easier to reuse, update, and understand.

2. How many pillars are there in OOP? Name all of them.

Encapsulation – Keeping data and methods together in one place, and hiding the internal details from the outside.

Abstraction – Hiding complex code and showing only the necessary parts.

Inheritance – Allowing one class to take on the properties and methods of another.

Polymorphism – Allowing different classes to use the same method name but behave differently.


3. What are the main parts of a class?
Attributes : Hold the data for the object.

Methods: Functions that define the behaviors of the object.

Constructor __init__ method: A special method used to initialize an object’s attributes when it is created.

Self keyword: Refers to the current instance of the class.


4. How do we create a class in Python?
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")
5. What is the difference between a class and an object?

A class is like a blueprint – it defines how something should behave and what it should have.

An object is a specific instance created from that class – it's the actual thing built from the blueprint.