def my_first_func():
    pass

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."


if __name__ == "__main__":
    dog = Dog("Buddy", 3)
    print(dog.speak())
    
    cat = Cat("Whiskers", 2)
    print(cat.speak())
