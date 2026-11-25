#Write a Python program to show single inheritance using classes Animal and Dog.
class Animal:
    def eat(self):
        print("Animals eat food to survive.")
class Dog(Animal):
    def bark(self):
        print("Dog barks: Woof! Woof!")
if __name__ == "__main__":
    print("Single Inheritance")
    my_dog = Dog()
    my_dog.eat()
    my_dog.bark()
