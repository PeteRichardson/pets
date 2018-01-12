import unittest

from pets import Pet, Cat, Dog, Horse

class TestPet(unittest.TestCase):
	def test_cant_instantiate_pet(self):
		""" Pet is abstract and cant be instantiated """
		with self.assertRaises(TypeError):
			pet = Pet("Waldo", "Gerbil", 8, "Mongolian Gerbil")

class TestCat (unittest.TestCase):
	def setUp(self):
		self.samplecat = Cat("Bella", 3, "American Shorthair")

	def test_catsound(self):
		""" Cats should Meow """
		self.assertEqual(self.samplecat.sound, "Meow")

	def test_age_out_of_bounds(self):
		""" Ages outside of 0-25 should throw """
		with self.assertRaises(ValueError):
			unborncat = Cat("Fetus", 0, "Main Coon")

		with self.assertRaises(ValueError):
			oldcat = Cat("Methuselah", 40, "Egyptian Sphinx")

class TestDog(unittest.TestCase):
	def setUp(self):
		self.sampledog = Dog("Silly", 4, "Austrailan Shepherd")

	def test_dogsound(self):
		""" Dogs should Woof """
		self.assertEqual(self.sampledog.sound, "Woof")

class TestHorse(unittest.TestCase):
	def setUp(self):
		self.samplehorse = Horse("Pixie", 8, "Arabian")

	def test_dogsound(self):
		""" Horses should Neigh """
		self.assertEqual(self.samplehorse.sound, "Neigh")


if __name__ == "__main__":
	unittest.main()