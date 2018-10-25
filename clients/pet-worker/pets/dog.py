# -*- coding: utf-8 -*-

from pets import Pet

class Dog (Pet):
    breeds = ["Affenpinscher", "Afghan Hound", "Airedale Terrier", "Akita",
    "Alaskan Klee Kai", "Alaskan Malamute", "American Bulldog",
    "American English Coonhound", "American Eskimo Dog", "American Foxhound",
    "American Pit Bull Terrier", "American Staffordshire Terrier",
    "American Water Spaniel", "Anatolian Shepherd Dog", "Appenzeller Sennenhunde",
    "Australian Cattle Dog", "Australian Shepherd", "Australian Terrier",
    "Azawakh", "Barbet", "Basenji", "Basset Hound", "Beagle", "Bearded Collie", 
    "Bedlington Terrier", "Belgian Malinois", "Belgian Sheepdog",
    "Belgian Tervuren", "Berger Picard", "Bernedoodle", "Bernese Mountain Dog",
    "Bichon Frise", "Black and Tan Coonhound", "Black Mouth Cur",
    "Black Russian Terrier", "Bloodhound", "Bluetick Coonhound", "Boerboel",
    "Bolognese", "Border Collie", "Border Terrier", "Borzoi", "Boston Terrier",
    "Bouvier des Flandres", "Boxer", "Boykin Spaniel", "Bracco Italiano", 
    "Briard", "Brittany", "Brussels Griffon", "Bull Terrier",
    "Bulldog", "Bullmastiff", "Cairn Terrier", "Canaan Dog", "Cane Corso",
    "Cardigan Welsh Corgi", "Catahoula Leopard Dog", "Caucasian Shepherd Dog", 
    "Cavalier King Charles Spaniel", "Cesky Terrier", "Chesapeake Bay Retriever",
    "Chihuahua", "Chinese Crested", "Chinese Shar-Pei",
    "Chinook", "Chow Chow", "Clumber Spaniel", "Cockapoo", "Cocker Spaniel",
    "Collie", "Coton de Tulear", "Curly-Coated Retriever", "Dachshund",
    "Dalmatian", "Dandie Dinmont Terrier", "Doberman Pinscher", "Dogo Argentino",
    "Dogue de Bordeaux", "Dutch Shepherd", "English Cocker Spaniel", 
    "English Foxhound", "English Setter", "English Springer Spaniel", 
    "English Toy Spaniel", "Entlebucher Mountain Dog", "Field Spaniel", 
    "Finnish Lapphund", "Finnish Spitz", "Flat-Coated Retriever",
    "Fox Terrier", "French Bulldog", "German Pinscher", "German Shepherd Dog", 
    "German Shorthaired Pointer", "German Wirehaired Pointer", "Giant Schnauzer",
    "Glen of Imaal Terrier", "Goldador", "Golden Retriever",
    "Goldendoodle", "Gordon Setter", "Great Dane", "Great Pyrenees",
    "Greater Swiss Mountain Dog", "Greyhound", "Harrier", "Havanese",
    "Ibizan Hound", "Icelandic Sheepdog", "Irish Red and White Setter",
    "Irish Setter", "Irish Terrier", "Irish Water Spaniel", "Irish Wolfhound", 
    "Italian Greyhound", "Jack Russell Terrier", "Japanese Chin", "Keeshond",
    "Kerry Blue Terrier", "Komondor", "Kooikerhondje",
    "Korean Jindo Dog", "Kuvasz", "Labradoodle", "Labrador Retriever",
    "Lakeland Terrier", "Lancashire Heeler", "Leonberger", "Lhasa Apso",
    "Lowchen", "Maltese", "Maltese Shih Tzu", "Maltipoo", "Manchester Terrier",
    "Mastiff", "Miniature Pinscher", "Miniature Schnauzer",
    "Mutt", "Neapolitan Mastiff", "Newfoundland", "Norfolk Terrier",
    "Norwegian Buhund", "Norwegian Elkhound", "Norwegian Lundehund",
    "Norwich Terrier", "Nova Scotia Duck Tolling Retriever",
    "Old English Sheepdog", "Otterhound", "Papillon", "Peekapoo", "Pekingese",
     "Pembroke Welsh Corgi", "Petit Basset Griffon Vendeen", "Pharaoh Hound", "Plott",
    "Pocket Beagle", "Pointer", "Polish Lowland Sheepdog", "Pomeranian",
    "Pomsky", "Poodle", "Portuguese Water Dog", "Pug", "Puggle", "Puli",
    "Pyrenean Shepherd", "Rat Terrier", "Redbone Coonhound",
    "Rhodesian Ridgeback", "Rottweiler", "Saint Bernard", "Saluki", "Samoyed",
    "Schipperke", "Schnoodle", "Scottish Deerhound", "Scottish Terrier",
    "Sealyham Terrier", "Shetland Sheepdog", "Shiba Inu", "Shih Tzu",
    "Siberian Husky", "Silky Terrier", "Skye Terrier", "Sloughi",
    "Small Munsterlander Pointer", "Soft Coated Wheaten Terrier", "Stabyhoun",
    "Staffordshire Bull Terrier", "Standard Schnauzer", "Sussex Spaniel",
    "Swedish Vallhund", "Tibetan Mastiff", "Tibetan Spaniel", "Tibetan Terrier",
    "Toy Fox Terrier", "Treeing Tennessee Brindle", "Treeing Walker Coonhound",
    "Vizsla", "Weimaraner", "Welsh Springer Spaniel",
    "Welsh Terrier", "West Highland White Terrier", "Whippet", 
    "Wirehaired Pointing Griffon", "Xoloitzcuintli", "Yorkipoo",
    "Yorkshire Terrier" ]

    species = "Dog"

    def __init__(self, name=None, age=None, breed=None):
        super(Dog, self).__init__(Dog.species, name=name, age=age, breed=breed)
    
    @property
    def sound(self):
       return "Woof"


if __name__ == "__main__":
    silly = Dog("Silly", 4, "Australian Shepherd")
    silly.speak()
  