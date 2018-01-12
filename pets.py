class Pet:
	def __init__(self, name, species, age, breed, owner=None):
		self.name = name
		self.species = species
		self.age = age
		self.breed = breed
		self.owner = owner
		self.sound = ""

	def speak(self):
		print("{} the {} says '{}!'".format(self.name, self.species.lower(), self.sound))

class Cat (Pet):
	def __init__(self, name, age, breed, owner=None):
		super().__init__(name, "Cat", age, breed, owner)
		self.sound = "Meow"

class Dog (Pet):
	def __init__(self, name, age, breed, owner=None):
		super().__init__(name, "Dog", age, breed, owner)
		self.sound = "Woof"

if __name__ == "__main__":
	bella = Cat("Bella", 3, "American Shorthair", None)
	bella.speak()
	silly = Dog("Silly", 4, "Australian Shepherd", None)
	silly.speak()