# Polymorphism Example

class Bird:
    def sound(self):
        print("Birds chirp.")

class Cat:
    def sound(self):
        print("Cats meow.")

def make_sound(animal):
    animal.sound()

bird = Bird()
cat = Cat()

make_sound(bird)
make_sound(cat)