# parent class
class Animal:
    def speak(self):
        print("Animal is speaking")

class  Dog (Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal) :
    def meaw(self):
        print("Cat is meawing")

d = Dog()
d.speak()

c = Cat()
c.meaw()

