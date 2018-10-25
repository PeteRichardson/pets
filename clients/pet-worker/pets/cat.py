# -*- coding: utf-8 -*-

from pets import Pet

class Cat (Pet):
    breeds = [ "Abyssinian", "American Bobtail",
    "American Curl", "American Shorthair", "American Wirehair", "Balinese",
    "Bengal Cats", "Birman", "Bombay", "British Shorthair", "Burmese",
    "Burmilla", "Chartreux", "Chinese Li Hua", "Colorpoint Shorthair",
    "Cornish Rex", "Cymric", "Devon Rex", "Egyptian Mau", "European Burmese",
    "Exotic", "Havana Brown", "Himalayan", "Japanese Bobtail",
    "Javanese", "Korat", "LaPerm", "Maine Coon", "Manx", "Nebelung",
    "Norwegian Forest", "Ocicat", "Oriental", "Persian", "Pixie-Bob",
    "Ragamuffin", "Ragdoll Cats", "Russian Blue", "Savannah", "Scottish Fold",
    "Selkirk Rex", "Siamese Cat", "Siberian", "Singapura",
    "Snowshoe", "Somali", "Sphynx", "Tonkinese", "Turkish Angora", "Turkish Van"]

    species = "Cat"

    def __init__(self, name=None, age=None, breed=None):
        super(Cat, self).__init__(Cat.species, name=name, age=age, breed=breed)
    
    @property
    def sound(self):
        return "Meow"


if __name__ == "__main__":
    bella = Cat("Bella", 3, "American Shorthair")
    bella.speak()
