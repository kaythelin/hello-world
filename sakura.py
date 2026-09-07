def my_first_func():
    pass

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."


if __name__ == "__main__":
    dog = Dog("Buddy")
    print(dog.speak())
