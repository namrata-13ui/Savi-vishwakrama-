# Inheritance Example

class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof Woof!")

dog = Dog()

dog.sound()
dog.bark()