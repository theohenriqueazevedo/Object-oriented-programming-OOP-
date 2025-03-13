# inheritance.py

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} barks: Woof!")

def main():
    generic_animal = Animal("Generic Animal")
    generic_animal.speak()

    dog = Dog("Buddy")
    dog.speak()

if __name__ == "__main__":
    main()
