from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name, species, age, breed):
        self.name = name
        self.species = species
        self.age = age
        self.breed = breed      

        if not 0 < self.age < 25:
            raise ValueError("Invalid age... {}. Expected 0 < age < 25".format(self.age))

    @property
    @abstractmethod
    def sound(self):
        pass

    def speak(self):
        print("{} the {} says '{}!'".format(self.name, self.species.lower(), self.sound))

class Cat (Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, "Cat", age, breed)
    
    @property
    def sound(self):
        return "Meow"

class Dog (Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age, breed)
    
    @property
    def sound(self):
       return "Woof"

if __name__ == "__main__":
    bella = Cat("Bella", 3, "American Shorthair")
    bella.speak()
    silly = Dog("Silly", 4, "Australian Shepherd")
    silly.speak()