# -*- coding: utf-8 -*-

from pets import Pet

class Snake (Pet):
    breeds = [  "King Cobra",
                "American Copperhead",
                "Black Mamba",
                "Corn Snake",
                "Rattlesnake",
                "Boa Constrictor",
                "Eastern Coral Snake",
                "Black Rat Snake",
                "Burmese Python",
                "Ball Python",
                "Royal Python",
                "Reticulated Python",
                "Garter Snake",
                "Green Anaconda",
                "Water Moccasin Snake",
                "Green Tree Python"]
    
    species = "Snake"

    max_age = 25

    def __init__(self, name=None, age=None, breed=None):
        super(Snake, self).__init__(Snake.species, name=name, age=age, breed=breed)
    
    @property
    def sound(self):
       return "Hisss"

if __name__ == "__main__":
    striker = Snake("Striker", 6, "Rattlesnake")
    striker.speak()