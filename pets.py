# -*- coding: utf-8 -*-

from random import choice, randrange
import json

class Pet(object):
    species = None   # Generic Pet has no species

    def __init__(self, species, name=None, age=None, breed=None):
        if not name:
            name = choice(Pet.names)
        if not breed:
            breed = choice(self.breeds)
        if age is None:
            age = randrange(1,24)

        self.name = name
        self.species = species
        self.age = age
        self.breed = breed      

        if not 0 < self.age < 25:
            raise ValueError("Invalid age... {}. Expected 0 < age < 25".format(self.age))

    @property
    def sound(self):
        pass

    def speak(self):
        print("{} the {} says '{}!'".format(self.name, self.species.lower(), self.sound))

    def __str__(self):
        return json.dumps(self.__dict__)

    names = [ "Abbey", "Abbie", "Abby", "Abel", "Abigail", "Ace",
    "Adam", "Addie", "Admiral", "Aggie", "Aires", "Aj", "Ajax", "Aldo",
    "Alex", "Alexus", "Alf", "Alfie", "Allie", "Ally", "Amber", "Amie",
    "Amigo", "Amos", "Amy", "Andy", "Angel", "Angus", "Annie", "Apollo",
    "April", "Archie", "Argus", "Aries", "Armanti", "Arnie", "Arrow",
    "Ashes", "Ashley", "Astro", "Athena", "Atlas", "Audi", "Augie",
    "Aussie", "Austin", "Autumn", "Axel", "Axle", "Babbles", "Babe",
    "Baby-Doll", "Baby", "Babykins", "Bacchus", "Bailey", "Bam-Bam",
    "Bambi", "Bandit", "Banjo", "Barbie", "Barclay", "Barker",
    "Barkley", "Barley", "Barnaby", "Barney", "Baron", "Bart", "Basil",
    "Baxter", "Bb", "Beamer", "Beanie", "Beans", "Bear", "Beau",
    "Beauty", "Beaux", "Bebe", "Beetle", "Bella", "Belle", "Ben",
    "Benji", "Benny", "Benson", "Bentley", "Bernie", "Bessie", "Biablo",
    "Bibbles", "Big Boy", "Big Foot", "Biggie", "Billie", "Billy",
    "Bingo", "Binky", "Birdie", "Birdy", "Biscuit", "Bishop", "Bits",
    "Bitsy", "Bizzy", "Bj", "Black-Jack", "Blackie", "Blanche", "Blast",
    "Blaze", "Blondie", "Blossom", "Blue", "Bo", "Bob", "Bobbie",
    "Bobby", "Bobo", "Bodie", "Bogey", "Bones", "Bongo", "Bonnie", "Boo-Boo",
    "Boo", "Booker", "Boomer", "Boone", "Booster", "Bootie",
    "Boots", "Boozer", "Boris", "Bosco", "Bosley", "Boss", "Boy",
    "Bozley", "Bradley", "Brady", "Braggs", "Brandi", "Brando",
    "Brandy", "Bridgett", "Bridgette", "Brie", "Brindle", "Brit",
    "Brittany", "Brodie", "Brook", "Brooke", "Brownie", "Bruiser",
    "Bruno", "Brutus", "Bubba", "Bubbles", "Buck", "Buckeye", "Bucko",
    "Bucky", "Bud", "Budda", "Buddie", "Buddy Boy", "Buddy", "Buffie",
    "Buffy", "Bug", "Bugsey", "Bugsy", "Bullet", "Bullwinkle", "Bully",
    "Bumper", "Bunky", "Buster-Brown", "Buster", "Butch", "Butchy",
    "Butter", "Butterball", "Buttercup", "Butterscotch", "Buttons",
    "Buzzy", "Caesar", "Cali", "Callie", "Calvin", "Cameo", "Camille",
    "Candy", "Capone", "Captain", "Carley", "Casey", "Casper", "Cassie",
    "Cassis", "Cha Cha", "Chad", "Chamberlain", "Champ", "Chance",
    "Chanel", "Chaos", "Charisma", "Charles", "Charlie Brown",
    "Charlie", "Charmer", "Chase", "Chauncey", "Chaz", "Checkers",
    "Chelsea", "Cherokee", "Chessie", "Chester", "Chevy", "Chewie",
    "Chewy", "Cheyenne", "Chi Chi", "Chic", "Chico", "Chief", "Chili",
    "China", "Chip", "Chipper", "Chippy", "Chips", "Chiquita", "Chivas",
    "Chloe", "Chocolate", "Chrissy", "Chubbs", "Chucky", "Chyna",
    "Cinder", "Cindy", "Cinnamon", "Cisco", "Claire", "Clancy", "Cleo",
    "Cleopatra", "Clicker", "Clifford", "Clover", "Clyde", "Coal",
    "Cobweb", "Coco", "Cocoa", "Coconut", "Codi", "Cody", "Cole",
    "Comet", "Commando", "Conan", "Connor", "Cookie", "Cooper",
    "Copper", "Corky", "Cosmo", "Cotton", "Cozmo", "Crackers",
    "Cricket", "Crystal", "Cubby", "Cubs", "Cujo", "Cupcake", "Curly",
    "Curry", "Cutie-Pie", "Cutie", "Cyrus", "Daffy", "Daisey-Mae",
    "Daisy", "Dakota", "Dallas", "Dandy", "Dante", "Daphne", "Darby",
    "Darcy", "Darwin", "Dash", "Dave", "Deacon", "Dee Dee", "Dee",
    "Dempsey", "Destini", "Dewey", "Dexter", "Dharma", "Diamond",
    "Dickens", "Diego", "Diesel", "Digger", "Dillon", "Dinky", "Dino",
    "Diva", "Dixie", "Dobie", "Doc", "Dodger", "Doggon", "Dolly",
    "Domino", "Doodles", "Doogie", "Dots", "Dottie", "Dozer",
    "Dragster", "Dreamer", "Duchess", "Dude", "Dudley", "Duffy", "Duke",
    "Duncan", "Dunn", "Dusty", "Dutches", "Dutchess", "Dylan", "Earl",
    "Ebony", "Echo", "Eddie", "Eddy", "Edgar", "Edsel", "Eifel",
    "Einstein", "Ellie", "Elliot", "Elmo", "Elvis", "Elwood", "Ember",
    "Emily", "Emma", "Emmy", "Erin", "Ernie", "Eva", "Faith", "Fancy",
    "Felix", "Fergie", "Ferris", "Fido", "Fifi", "Figaro", "Finnegan",
    "Fiona", "Flake", "Flakey", "Flash", "Flint", "Flopsy", "Flower",
    "Floyd", "Fluffy", "Fonzie", "Foxy", "Francais", "Frankie",
    "Franky", "Freckles", "Fred", "Freddie", "Freddy", "Freedom",
    "Freeway", "Fresier", "Friday", "Frisco", "Frisky", "Fritz",
    "Frodo", "Frosty", "Furball", "Fuzzy", "Gabby", "Gabriella",
    "Garfield", "Gasby", "Gator", "Gavin", "Genie", "George", "Georgia",
    "Georgie", "Giant", "Gibson", "Gidget", "Gigi", "Gilbert", "Gilda",
    "Ginger", "Ginny", "Girl", "Gizmo", "Godiva", "Goldie", "Goober",
    "Goose", "Gordon", "Grace", "Gracie", "Grady", "Greenie", "Greta",
    "Gretchen", "Gretel", "Gretta", "Griffen", "Gringo", "Grizzly",
    "Gromit", "Grover", "Gucci", "Guido", "Guinness", "Gunner",
    "Gunther", "Gus", "Guy", "Gypsy", "Hailey", "Haley", "Hallie",
    "Hamlet", "Hammer", "Hank", "Hanna", "Hannah", "Hans", "Happyt",
    "Hardy", "Harley", "Harpo", "Harrison", "Harry", "Harvey",
    "Heather", "Heidi", "Henry", "Hercules", "Hershey", "Higgins",
    "Hobbes", "Holly", "Homer", "Honey-Bear", "Honey", "Hooch",
    "Hoover", "Hope", "Houdini", "Howie", "Hudson", "Huey", "Hugh",
    "Hugo", "Humphrey", "Hunter", "India", "Indy", "Iris", "Isabella",
    "Isabelle", "Itsy-Bitsy", "Itsy", "Ivory", "Ivy", "Izzy", "Jack",
    "Jackie", "Jackpot", "Jackson", "Jade", "Jagger", "Jags", "Jaguar",
    "Jake", "Jamie", "Jasmine", "Jasper", "Jaxson", "Jazmie", "Jazz",
    "Jelly-Bean", "Jelly", "Jenna", "Jenny", "Jerry", "Jersey", "Jess",
    "Jesse James", "Jesse", "Jessie", "Jester", "Jet", "Jethro", "Jett",
    "Jetta", "Jewel", "Jewels", "Jimmuy", "Jingles", "Jj", "Joe",
    "Joey", "Johnny", "Jojo", "Joker", "Jolie", "Jolly", "Jordan",
    "Josie", "Joy", "Jr", "Judy", "Julius", "June", "Junior", "Justice",
    "Kali", "Kallie", "Kane", "Karma", "Kasey", "Katie", "Kato", "Katz",
    "Kayla", "Kc", "Keesha", "Kellie", "Kelly", "Kelsey", "Kenya",
    "Kerry", "Kibbles", "Kid", "Kiki", "Killian", "King", "Kipper",
    "Kira", "Kirby", "Kismet", "Kissy", "Kitty", "Kiwi", "Klaus",
    "Koba", "Kobe", "Koda", "Koko", "Kona", "Kosmo", "Koty", "Kramer",
    "Kujo", "Kurly", "Kyra", "Lacey", "Laddie", "Lady", "Ladybug",
    "Laney", "Lassie", "Latte", "Layla", "Lazarus", "Lefty", "Leo",
    "Levi", "Lexi", "Lexie", "Lexus", "Libby", "Lightning", "Lili",
    "Lilly", "Lily", "Lincoln", "Linus", "Little Bit", "Little-Guy",
    "Little-One", "Little-Rascal", "Lizzy", "Logan", "Loki", "Lola",
    "Lou", "Louie", "Louis", "Lovey", "Lucas", "Luci", "Lucifer",
    "Lucky", "Lucy", "Luke", "Lulu", "Luna", "Lynx", "Mac", "Macho",
    "Macintosh", "Mack", "Mackenzie", "Macy", "Maddie", "Maddy",
    "Madison", "Maggie-Mae", "Maggie-Moo", "Maggie", "Maggy", "Magic",
    "Magnolia", "Major", "Mandi", "Mandy", "Mango", "Marble", "Mariah",
    "Marley", "Mary Jane", "Mary", "Mason", "Mattie", "Maverick", "Max",
    "Maximus", "Maxine", "Maxwell", "May", "Maya", "Mcduff", "Mckenzie",
    "Meadow", "Megan", "Meggie", "Mercedes", "Mercle", "Merlin", "Mia",
    "Miasy", "Michael", "Mickey", "Midnight", "Mikey", "Miko", "Miles",
    "Miller", "Millie", "Milo", "Mimi", "Mindy", "Ming", "Mini",
    "Minnie", "Mischief", "Misha", "Miss Kitty", "Miss Priss", "Missie",
    "Missy", "Mister", "Misty", "Mitch", "Mo", "Mocha", "Mojo",
    "Mollie", "Molly", "Mona", "Monkey", "Monster", "Montana",
    "Montgomery", "Monty", "Moocher", "Moochie", "Mookie", "Moonshine",
    "Moose", "Morgan", "Moses", "Mouse", "Mr Kitty", "Muffin", "Muffy",
    "Mugsy", "Mulligan", "Munchkin", "Murphy", "Nakita", "Nala", "Nana",
    "Napoleon", "Natasha", "Nathan", "Nellie", "Nemo", "Nena", "Nero",
    "Nestle", "Newt", "Newton", "Nibbles", "Nibby-Nose", "Nibby",
    "Nick", "Nickers", "Nickie", "Nicky", "Nico", "Nike", "Niki",
    "Nikita", "Nikki", "Niko", "Nina", "Nitro", "Nobel", "Noel", "Nona",
    "Noodles", "Norton", "Nosey", "Nugget", "Nutmeg", "Oakley", "Obie",
    "Odie", "Old Glory", "Olive", "Oliver", "Olivia", "Ollie", "Onie",
    "Onyx", "Opie", "Oreo", "Oscar", "Otis", "Otto", "Oz", "Ozzie",
    "Ozzy", "Pablo", "Paco", "Paddington", "Paddy", "Panda", "Pandora",
    "Panther", "Papa", "Paris", "Parker", "Pasha", "Patch", "Patches",
    "Patricky", "Patsy", "Patty", "Peaches", "Peanut", "Peanuts",
    "Pearl", "Pebbles", "Pedro", "Penny", "Pepe", "Pepper", "Peppy",
    "Pepsi", "Persy", "Persephone", "Pete", "Peter", "Petey", "Petie", "Phantom",
    "Phoebe", "Phoenix", "Picasso", "Pickles", "Pierre", "Piggy",
    "Piglet", "Pink Panther", "Pinky", "Pinto", "Pip-Squeek", "Piper",
    "Pippin", "Pippy", "Pirate", "Pixie", "Plato", "Pluto", "Pockets",
    "Pogo", "Pokey", "Polly", "Poncho", "Pongo", "Pooch", "Poochie",
    "Pooh-Bear", "Pooh", "Pookie", "Pooky", "Popcorn", "Poppy",
    "Porche", "Porkchop", "Porky", "Porter", "Powder", "Prancer",
    "Precious", "Presley", "Pretty-Girl", "Pretty", "Prince",
    "Princess", "Prissy", "Puck", "Puddles", "Pudge", "Puffy",
    "Pugsley", "Pumpkin", "Punkin", "Puppy", "Purdy", "Queen",
    "Queenie", "Quincy", "Quinn", "Rags", "Raison", "Ralph", "Ralphie",
    "Rambler", "Rambo", "Ranger", "Rascal", "Raven", "Rebel", "Red",
    "Reggie", "Reilly", "Remy", "Rex", "Rexy", "Rhett", "Ricky", "Rico",
    "Riggs", "Riley", "Rin Tin Tin", "Ringo", "Ripley", "Rocco", "Rock",
    "Rocket", "Rocko", "Rocky", "Roland", "Rolex", "Rollie", "Roman",
    "Romeo", "Rosa", "Roscoe", "Rosebud", "Rosie", "Rosy", "Rover",
    "Rowdy", "Roxanne", "Roxie", "Roxy", "Ruby", "Ruchus", "Rudy",
    "Ruffe", "Ruffer", "Ruffles", "Rufus", "Ruger", "Rusty", "Ruthie",
    "Ryder", "Sabine", "Sable", "Sabrina", "Sadie", "Sage", "Sailor",
    "Salem", "Sally", "Salty", "Sam", "Samantha", "Sammy", "Sampson",
    "Samson", "Sandy", "Sara", "Sarah", "Sarge", "Sasha", "Sassie",
    "Sassy", "Savannah", "Sawyer", "Scarlett", "Schotzie", "Schultz",
    "Scoobie", "Scooby-Doo", "Scooby", "Scooter", "Scottie", "Scout",
    "Scrappy", "Scruffy", "Sebastian", "Shadow", "Shady", "Shaggy",
    "Shasta", "Sheba", "Sheena", "Shelby", "Shelly", "Sherman",
    "Shiloh", "Shiner", "Shorty", "Sienna", "Sierra", "Silky", "Silver",
    "Silvester", "Simba", "Simon", "Simone", "Sissy", "Skeeter",
    "Skinny", "Skip", "Skipper", "Skippy", "Skittles", "Sky", "Skye",
    "Skyler", "Slick", "Slinky", "Sly", "Smarty", "Smokey","Smokey",
    "Smudge", "Sneakers", "Snickers", "Snoop", "Snoopy", "Snowball",
    "Snowflake", "Snowy", "Snuffles", "Snuggles", "Solomon", "Sonny",
    "Sophia", "Sophie", "Sox", "Spanky", "Sparkle", "Sparky", "Speed",
    "Speedo", "Speedy", "Spencer", "Spike", "Spirit", "Spookey", "Spot",
    "Spotty", "Spud", "Spunky", "Squeeky", "Squirt", "Stanley", "Star",
    "Starr", "Stella", "Sterling", "Stich", "Stinky", "Stormy",
    "Stuart", "Sugar-Baby", "Sugar", "Summer", "Sumo", "Sundance",
    "Sunday", "Sunny", "Sunshine", "Susie-Q", "Susie", "Suzy", "Sweet-Pea",
    "Sweetie-Pie", "Sweetie", "Sydney", "T-Bird", "T-Bone",
    "Tabby", "Tabetha", "Taco", "Taffy", "Tally", "Tammy", "Tangles",
    "Tango", "Tank", "Tanner", "Tara", "Tasha", "Taylor", "Taz", "Teddy-Bear",
    "Teddy", "Tequila", "Tess", "Tessa", "Tessie", "Tex",
    "Thelma", "Thor", "Thumper", "Thunder", "Thyme", "Tiffany", "Tiger",
    "Tigger", "Tiggy", "Tiki", "Tilly", "Timber", "Timmy", "Tinker-Bell",
    "Tinker", "Tinky", "Tiny", "Tippy", "Tipr", "Titan", "Tito",
    "Titus", "Tobie", "Toby", "Toffee", "Tom", "Tommy-Boy", "Tommy",
    "Toni", "Tony", "Toots", "Tootsie", "Topaz", "Tori", "Toto",
    "Tracker", "Tramp", "Trapper", "Travis", "Trigger", "Trinity",
    "Tripod", "Tristan", "Trixie", "Trooper", "Trouble", "Troy",
    "Truffles", "Tuck", "Tucker", "Tuesday", "Tuffy", "Turbo", "Turner",
    "Tux", "Twiggy", "Twinkle", "Ty", "Tyler", "Tyson", "Valinto",
    "Vava", "Vegas", "Velvet", "Vinnie", "Vinny", "Violet", "Vito",
    "Volvo", "Waddles", "Wags", "Waldo", "Wallace", "Wally", "Walter",
    "Wayne", "Weaver", "Webster", "Wesley", "Westie", "Whiskers",
    "Whiskey", "Whispy", "Whitie", "Whiz", "Wiggles", "Wilber",
    "Willie", "Willow", "Willy", "Wilson", "Winnie", "Winston",
    "Winter", "Wiz", "Wizard", "Wolfgang", "Wolfie", "Woody", "Woofie",
    "Wrigley", "Wrinkles", "Wyatt", "Xena", "Yaka", "Yang", "Yeller",
    "Yellow", "Yin", "Yoda", "Yogi-Bear", "Yogi", "Yukon", "Zack",
    "Zeke", "Zena", "Zeus", "Ziggy", "Zippy", "Zoe", "Zoey", "Zoie",
    "Zorro"]
   
    @classmethod
    def random(cls):
        if cls.__name__ == "Pet":
            # pick a class from all the subclasses of pet
            clas = choice(cls.__subclasses__())
        else:
            # pick the class the user specified
            clas = globals()[cls.species]
        return clas()

    def json(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return self.json()


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
        super(Cat, self).__init__(Cat.species, name, age, breed)
    
    @property
    def sound(self):
        return "Meow"

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
        super(Dog, self).__init__(Dog.species, name,  age, breed)
    
    @property
    def sound(self):
       return "Woof"

class Horse (Pet):
    breeds = [ "Abaco Barb", "Abstang", "Abtenauer", "Abyssinian", "Adaev",
    "Aegidienberger", "Ainos Pony", "Akhal-Teke", "Albanian Horse", "Altai",
    "Alter Real", "Altmarkisches Kaltblut", "Altwurttemberg", "American Albino",
    "American Bashkir", "American Cream Draft", "American Drum Horse",
    "American Indian Horse", "American Mammoth Jack", "American Miniature Horse",
    "American Mustang", "American Paint Horse", "American Quarter Horse",
    "American Saddlebred", "American Shetland", "American Sport Pony",
    "American Spotted Paso", "American Standardbred", "American Thoroughbred",
    "American Walking Pony", "American Warmblood", "Amur", "Anadolu Pony",
    "Andalusian", "Andean", "Andino Pony", "Andravida", "Anglo-Arabian",
    "Anglo-Arabo-Sardo", "Anglo-Kabarda", "Anglo-Karachai", "Anglo-Luso",
    "Anglo-Norman", "Appaloosa", "Appaloosa Sport Horse", "Appendix Quarter Horse", "AraAppaloosa", "Arabian",
    "Arabian-Berber", "Arabian-Haflinger", "Arabo-Friesian", "Araboulonnais", "Aralusian", "Ardahan", "Ardennes",
    "Arenberg-Nordkirchener", "Argentine Anglo", "Argentine Criollo", "Argentine Polo Pony", "Argentinean Modepony", "Argentinian Ranch Horse", "Ariegeois Pony", "Arravani", "Asiatic Wild Horse", "Asil", "Assateague Pony", "Astrakhan", "Asturcón", "Asturian", "Australian Brumby", "Australian Draught", "Australian Pony",
    "Australian Stock horse", "Australian Warmblood", "Austrian Warmblood", "Autre Que Pur Sang", "Auxois", "Avelignese", "Azerbaijan",
    "Azores", "Azteca", "Baguales", "Baguio Light Horse", "Baguio Pony", "Bahr-El-Ghazal", "Baikal", "Baise", "Baixadeiro Horse", "Bajau Pony", "Bakhtiari", "Baladi", "Balearic Horse", "Bali Pony", "Balikun Horse", "Baluchi Horse", "Ban-ei", "Banamba", "Banat", "Bandiagara", "Banker Pony", "Barb", "Bardigiano", "Barra", "Bara Pony", "Barthais Pony", "Bashkir Horse", "Basotho Pony", "Basuto Pony", "Basque Pony", "Batak Pony", 
    "Bavarian Warmblood", "Beledougou", "Belgian Ardennais", "Belgian Draft", "Belgian Sport Horse", "Belgian Halfblood", "Belgian Warmblood", "Bergmann Pony", "Bhorum Pony", "Bhotia Pony", "Bhutia Pony", "Bidet Horse", "Bigourdan Horse", "Bitcuk", "Black Forest Horse", "Black Sea Horse", "Blazer Horse", "Boerperd", "Bolivian Pony", "Borneo Pony", "Bose Pony", "Bosnian Pony", "Boulonnais", "Brabant", "Barbancon", "Brandenburger", "Brazilian Pony", "Brazilian Sport Horse", 
    "Breton", "British Appaloosa", "British Riding Pony", "British Shetland", "British Spotted Pony", "British Thoroughbred", "British Warmblood", "Brumby", "Buckskin", "Bucovina", "Budyonny", "Bulgarian Native Horse", "Buohai", "Burmese Pony",
    "Buryat", "Busak Posavec", "Byelorussian Harness Horse", "Calabrese", "Calvinia Horse", "Camargue Horse", "Camarillo White Horse", "Campeiro", "Campolina", "Canadian Cutting Horse", "Canadian Horse", 
    "Canadian Pacer", "Canadian Rustic Pony", "Canadian Sport Horse", "Canadian Hunter", "Canadian Warmblood", "Canik", "Cape Harness", "Cape Horse", "Carolina Marsh Tacky", "Carpathian Pony", "Carthusian Horse", "Caspian", "Castilian Horse", "Catria Horse", "Cayuse Pony", "Celtic Pony", "Cerbat Mustang", "Certisino", "Chahou Post Pony", "Chaidamu Pony", "Chakouyi", "Chalosse Pony", "Champagne Horse", "Chamurthi", 
    "Chapman Horse", "Charentais", "Charollais", "Charysh", "Chara", "Cheju Pony", "Cheval de Corlay", "Cheval Demi sang du Centre", "Cheval d’Auvergne", "Chickasaw Horse", "Chicksaw Pony", "Chilean Corralero", "Chilkow", "Chilote Pony", "Chincoteague Pony", "Choctaw Horse", "Chumbivilcas Horse", "Chumysh Horse", "Chyanta Pony", "Cimarron Horse", "Cleveland Bay", "Clydesdale", "Cob", "Coffin Bay Pony", "Coldblooded Trotter", "Colonial Spanish", "Colorado Ranger",
    "Comtois horse", "Conestoga Horse", "Connemara Pony", "Corajoso", "Corolla Island Pony", "Corsican Horse", "Cossak Horse", "Costa Rican Saddle Horse", "Country Saddle Horse", "Cretan Horse", "Criollo", "Crioulo", "Crioulo Brasileiro", "Croatian Hladnokrvnjak", "Croatian Posavac", "Cuban Paso", "Cuban Pinto", "Cukurova", "Curly Haired Fox Trotter", "Curly Horse", "Cutchi", "Czech Coldblood", "Czech Warmblood", 
    "Czechoslovakian Small Riding Horse", "Dagestan Pony", "Dahoman", "Dales Pony", "Daliboz Horse", "Deliboz", "Danish Sport Pony", "Danish Wamblood", "Danube Delta Horse", "Danubian", "Dunav", "Darashouri", "Darashouli", "Darfur Pony", "Dartmoor Pony", "Datong Horse", "Debao Pony", "Deli Pony", "Deliorman", "Deliormanski", "Desert Norman Horse", "Deutsches Reitpony", "Dilbaz", "Deliboz", 
    "Daliboz", "Delibozskaya", "Djamoi", "Djamonský Pony", "Djerma Horse", "Dolny-Iskar", "Don", "Donskaya", "Dongola", "Dongolah", "Dongolawi", "Dosanko Horse", "Drum Horse", "Dutch Draft", "Dutch Harness Horse", "Dutch Warmblood", "Dzhabe", "Døle Gudbrandsdal", "Dølehest", "Døle Trotter", "Dülmen Pony", "East Bulgarian Horse", "East Friesian Horse – Old Type", "East Friesian Warmblood", "East Prussian", "Edelbluthaflinger", 
    "Ege Midillisi", "Egyptian Arabian", "Egyptian Horse", "Einsiedler", "Eleia", "English Thoroughbred", "Equus Kinsky", "Equus Przewalskii", "Eriskay Pony", "Erlanbach", "Erlunchun", "Esperia Pony", "Estonian Draft", "Estonian Arden", "Estonian Native", "Exmoor Pony", "Faca Galizana", "Falabella", "Faroe Pony", "Faeroes Pony", "Faeroe Island Horse", "Fell Pony", "Finnhorse", "Finnish Universal", "Finnish Warmblood", "Fjord horse", "Flemish Horse", 
    "Fleuve", "Flores Pony", "Florida Cracker Horse", "Florida Horse", "Florida Cow Pony", "Foundation Quarter Horse", "Fouta Horse", "Foutanké",
    "Frederiksborg Horse", "Freiberger horse", "Franches Montagnes", "Freiberger", "French Anglo Arab", "French Ardennais", "French Cob", "French Saddle Pony", "French Saddlebred", "Halfblood", "French Sport Horse", "French Trotter", "Friesian", "Friesian Sporthorse", "Furioso Horse", "Gala Horse", 
    "Galiceño Pony", "Galician Pony", "Gallego", "Galaga", "Galloway Pony", "Galshar", "Garrano", "Garrano do Minho",
    "Gayoe Pony", "Gelderlander", "Gelderland", "Geogrgian Grand", "German Coach Horse", "German Cold-Blooded", "German Riding Pony", "Gharbaui", "Gharkawi", "Ghazi", "Giara", "Gidran", "Glasinacki", "Goklan", "Golden American Saddlebred", "Golden Horse of Bohemia", "Gotland Pony", "Grand Noir du Berry Donkey", "Great Black Berry Ass", "Great Poland Horse", "Greek Pony", 
    "Greyson Highlands Ponies", "Groningen Horse", "Groninger", "Guangxi Horse", "Guanxi", "Guanzhong", "Guba", "Guizhou Pony", "Guoxia Pony", "Gutsul", "Guculs", "Guzuls", "Gypsy Vanner", "Hackney Horse", "Hackney Pony", "Haflinger", "Half-Saddlebred", "Handachine Horse", "Hanoverian", "Hantam Horse", "Harddraver", "Holländischer", "Hardtdraver", "Harna", "Hazziz", "Hebridean Pony", "Heck Horse", "Heihe Horse", "Heilongkiang", "Henson Horse", "Hequ", "Hequl", "Hessen Horse", 
    "Hessischer", "Highland Pony", "Highlander Horse", "Hinis Horse", "Hinisin Kolu Kisasi Ati", "Hirzai", "Hispano", "Hispano Arabe", "Hmong Horse", "Hokkaido Pony", "Holsteiner",
    "Holsteiner Coldblood", "Horse of the Americas", "Hrvatski Hladnokrvnjak", "Hrvatski Posavac", "Hucul", "Huçul", "Hutsul", "Hutul", "Huculska", "Huzul ", "Hungarian Draft", "Hungarian Coldblood", "Hungarian Dun", "Hungarian Horse", "Hungarian Felver", "Ibérian Warmblood", "Icelandic Horse", "Ilia", "Indian Country Bred Horse", "Indian Horse", "Indian Pony", "International Striped Horse", "Iomud", "Iomudskaya", "Irish Cob", "Irish Draft", 
    "Irish Draught", "Irish Hobby", "Irish Hunter", "Irish Sport Horse", "Israeli Horse", "Italian Heavy Draft", "Italian Working Horse", "Italian Trotter", "Jabe", "Jaca Gallega", "Java Pony", "Jeju Pony", "Jennet", "Jianchang Pony", "Jielin Horse", "Jinhong Horse", "Jinzhou", "Jura", "Jutland", "Kabarda", "Kabardian", "Kabardinskaya", "Kagoshima", "Kuyshu", "Kaimanawa Horse", "Kaju Pony", "Kaldblodstraver", "Kalmyk", "Kalmykskaya", "Kandachi", "Kandachime",
    "Karabair", "Karabairskaya", "Karabakh", "Karabakhskaya", "Karacabey", "Karachai", "Karakachan Pony", "Karatschai Pony", "Karatschaever", "Karatschaewsker", "Karachaier", "Karakacan", "Kathiawari", "Kathi", "Kutchi", "Kazakh Horse", "Kazakhskaya", "Ke-Er-Qin", "Kentucky Mountain Saddle Horse", "Kerry Bog Pony", "Khani", "Kiger Mustang", "Kinsky Horse", 
    "Kirdi Pony", "Kirghiz", "Kirgizskaya", "Kisber Halfbred", "Kisber Felver", "Kiso Horse", 
    "Kladruby Horse", "Kladruber", "Kladrubsky", "Kleines Deutsches Reitpferd", "Klepper", "Knabstrupper", "Konik Horse", "Kordofani", "Kuda-Gayo", "Kumingan", "Kundudo", "Kushum", "Kushumakaya", "Kustanai", "Kustanair", "Kustanaiskaya", "Kuznetsk Horse", "KWPN", "Kyrgyz Horse", "Labem Horse", "Lac la Croix Indian Pony", "LLCIP", "Lakka", "Logone", "Landais Pony",
    "Latgale Trotter", "Latvian", "Latviiskaya", "Lehmkuhlener Pony", "Leutstetten", "Leutstettener", "Lewitzer Pony", "Lewitz Pony", "Lichuan", "Lijiang Pony",
    "Limousin Horse", "Lipizzan", "Lipizzaner", "Lippit Morgan", "Lithuanian Heavy Draft", "Lithuanian Landrace", "Little Poland Horse", "Ljutomer Trotter", "Llanero", "Lokai", "Lokaiskaya", "Lombok", "Losino", "Lundy Pony", "Lusitano", "Lyngen Horse", "Macassar", "Magyar Hidegveru", "Malakan Horse", "Mallorquin Horse", "Malopolski", "Mangalarga Marchador",
    "Mangalarga Paulista", "Manipuri Pony", "Marajoara", "Marajo", "Maremmano", "Maremmana Horse", "Marquesas Islands Horse", "Marsh Tacky", "Marwari", "Masuren", "Mazury", "Mecklenburg", "Mecklenburger Horse", "Megezh", "Megrel", "Mingrelian", "Megrelskaya", "Menorca", "Menorquin Horse", "Merens Pony", 
    "Messara Horse", "Metis Trotter", "Mezen", "Mezenskaya", "Mezohegyes Sport Horse", "Mimoseano",
    "Minho", "Miniature Horse", "Minusin Horse", "Misaki Pony", "Miyazaki", "Missouri Fox Trotting Horse", "Miyako Horse", "Miyazaki", "Mogod Pony", "Mongolian", "Mongolian Wild Horse", "Montana Travler", "Monterufoli Pony", "Morab", "Morgan Horse", "Morna", "Moroccan Barb", "Morochuco", "Mountain Pleasure Horse", "Mousseye Pony", "Mbai", "M’baye", "Mussey", "Moyle Horse", "Mulassier Horse", "Mura", "Mur Island", "Medjimurski", "Murakoz", "Murakosi", 
    "Murgese", "Murge Horse", "Musey Pony", "Mustang", "Mytilene Horse", "M’Bayar", "Namaqua Pony", "Nambu Horse",
    "Namib Desert Horse", "Nanfan", "Narragansett Pacer", "Narym", "Narymskaya", "National Show Horse", "Navarra", "Navarran", "Navarrais", "Navarre Pony", "Neapolitan", "Napolitan", "Napolitano Horse", "Nederlands Appaloosa Pony", "Nederlands Mini Paarden", "Dutch Mini Horse", "Nederlands Trekpaard", "Nefza", "New Forest Pony", "New Kirgiz Horse", "Novokirgizskaya", "Newfoundland Pony", "Nez Perce Horse", "Nigerian", "Nogai Horse", "Nokota Horse", "Noma Horse", "Nonius", "Noniusz", 
    "Nooitgedacht Pony", "Nordland Horse", "Norfolk Roadster", "Norfolk Trotter", "Noriker", "Noric", "Norman Cob", "Normandy Cob", "Norman Trotter", "North African Barb", "North Swedish Horse", "Nordsvensk Hast", "Northeastern", "Nordestino", "Northern Ardennais", "Northern Draft Horse", "Norwegian Fjord", "Norwegian Dun", "Norwegian Pony", "Northern Dun", "Norwegian Riding Pony",
    "Northlands", "Nordland-Lyngen", "Norwegian Trotter", "Novokirghiz", "Ob Pony", "Oberlander Horse", "Ocracoke",
    "Old Austrian Warmblood", "Old English Black Horse", "Old Kladruby Horse", "Oldenburger", "Oldenburg", "Orlov Trotter", "Orlovskaya Rysistaya",
    "Orlov-Rostopchin", "Oromo Horse", "Ostlandhester", "Outer Banks Ponies", "Padang Pony", "Paint Horse", "Paint Pony", "Palomino", "Pampa Horse", "Panela", "Peneia", "Pinia |Peneia", "Pineia", "Panje", "Panjeskaya", "Pantaneiro", "Poconeano", "Paso Fino", "Patibarcina Horse", "Pechora", "Pechorskaya", "Pentro", "Percheron", "Periangan Pony", "Perkehner Horse", "Persano Horse",
    "Peruvian Paso", "Petiso Pony", "Petiso Argentino", "Pindos Pony", "Pinkafo", "Pinkafeld Horse",
    "Pintabian", "Pinzgauer Horse", "Piquira Pony", "Pleven", "Plevna", "Plevenska", "Poitevin", "Polesian", "Polessakya", "Polish Konik", "Polish Primitive Horse", "Poney Gallego", "Poni Galaga", "Poney Mousseye", "Poneys Landais", "Pony of the Americas", "Posavina Horse", "Pottok", "Poznan Horse", "Prairie Horse", "Prairie Pony", "Priob", "Przewalski’s Horse", "Qatgani Horse", 
    "Quarab", "Quarter horse", "Quarter Pony", "Racking Horse", "Rahvan", "West Black Sea Rahvan Horse", "Rangerbred horse", 
    "Rhineland Heavy draft", "Rhenish Cold Blood", "Riwoche Pony", "Roadster", "Rocky Mountain Horse", "Romanian Saddle Horse", "Romanian Trotter", "Rottaler", "Rottal", "Rottaler Warmblut", "Russ", "Russian Don", "Russian Heavy Draft", "Russian Riding Horse", "Russian Trotter", "Sable Island Pony",
    "Sachsen Warmblood", "Sachsen Anhaltiner Warmblut", "Saddlebred", "Sadecki", "Salerno Horse", "Salernitano", "Samolaco", "San Fratello Horse", "Sanfratellani", "Sicilian Horse", "Sandalwood Pony", "Sandal", "Sandan Horse", "Sanhe", "Sardinian", "Sarcidano", "Sarvar", "Saxon-Turinga Coldblood", "Sächsisch-Thüringisches Kaltblut", "Saxony Warmblood", "Saxony-Thuringian Warmbloods", "Schleswiger Heavy Draft", 
    "Schleswiger Kaltblut", "Schwarzwälder Fuchs", "Scottish Galloway", "Selle Français", "Selle Français Pony", "Seminole Pony", "Senne Horse", "Senner", "Sertanejo",
    "Shackleford Banks Horse", "Shagya Arabian", "Shan Pony", "Sheehan", "Shetland Pony", "Shire Horse", "Silesian", "Slaski Horse", "Single-Footing Horse", "Sini", "Sining Horse",
    "Skogsruss", "Skyros Pony", "Slovak Sport Pony", "Slovak", "Slovakian Warmblood", "Sokolsky", "Sokolski", "Somali Pony", "Somme Bay Horse", "Sorraia", "South African Miniature", "South African Vlaamperd", "South African Warmblood", 
    "South German Coldblood", "Suddeutsches Kaltblut", "Soviet Heavy Draft", "Spanish Anglo-Arabian", "Spanish Barb", "Spanish Colonial Horse", "Spanish Jennet", "Spanish Mustang", "Spanish Norman", "Spiti Pony", "Spotted Saddle Horse", "Standardbred", "Strelets Horse", "Sudan Country-Bred", "Suffolk Punch", 
    "Sugarbush Draft", "Sulawesi", "Sumba Pony", "Sumbawa Pony", "Sunicho", "Swedish Ardennes", "Svensk Ardenner", "Swedish Warmblood", "Swedish Halfbred", "Swiss Warmblood", "Swiss Halfbred", "Süddeutsches Kaltblut", "Taishuh", "Taishu Horse", "Takhi Horse", "Tarbes", "Tarbais", "Tarpan", "Tavda", "Tavdinka", "Tavdinskaya",
    "Tawleed", "Tchenarani", "Tennessee Walking Horse", "Tennuvian", "Tersk", "Tersky", "Terskaya", "Thai Pony", "Thai Country Bred", "Thessalian", "Thessalonian", "Thoroughbred", "Thüringen Warmblood", "Tibetan Pony", "Tiger Horse", "Timor Pony", "Tinker Horse", "Tokara Pony", "Tokara Kyushu", "Tolfetano Horse", "Tori", "Tory", "Toric", "Toriiskaya", "Trait Du Nord", "Trakehner", "Trakya", "Tres Sangres", 
    "Three Blood", "Trote en Gallope", "Trote y Galope", "Trochador", "Trocha Horse", "Trottatore Italiano", "Trotteur Francais",
    "Tuigpaard", "Tuigpaarden", "Tunisian Pony", "Turk", "Turkoman", "Turkmene", "Turkmen", "Turkmenian", "Tushin", "Tuva", "Tuvan", "Tuvinskaya", "Tyrol Pesante Rapido", "Ukrainian Saddle-Riding Horse", "Unmol", "Upper Yenisei", "Uzunyayla Horse", "Venezuelan Criollo", "Ventasso Horse", "Vietnamese Hmong", "Virginia Highlander", "Vlaamperd", "Vladimir Heavy Draft",
    "Voronezh Coach", "Vyatka", "Viatka", "Waler", "Walkaloosa", "Washu Horse", "Welara Pony", "Welsh Cob ", "Welsh Mountain Pony ", "Welsh Pony", "Welsh Pony of Cob Type", "Weser-Ems Pony", "West African Barb", "West Norwegian", "West Norway",
    "Westland", "Western Sudan Pony", "Westfalen Pony", "Westfalen", "Westphalian", "Wielkopolski", "Wild Horses of the Namib", "Württemberger", "Xilingol", "Yabou", "Yaboo", "Yakut Horse", "Yamud", "Yanqi Horse", "Yemeni Horse", "Yili Horse", "Yonaguni Horse", "Yorkshire Coach Horse", "Yugoslav Mountain Pony", "Yunnan", "Yururi Island horse", "Zangersheide", "Zaniskari Pony",
    "Zeeland", "Zemaituka", "Zemaitukai", "Žemaitukas", "Zemaituka", "Zhumd", "Zhemaichu", "Zhmudk", "Zweibrucker"]
    
    species = "Horse"

    def __init__(self, name=None, age=None, breed=None):
        super(Horse, self).__init__(Horse.species, name, age, breed)
    
    @property
    def sound(self):
       return "Neigh"

if __name__ == "__main__":
    bella = Cat("Bella", 3, "American Shorthair")
    bella.speak()
    silly = Dog("Silly", 4, "Australian Shepherd")
    silly.speak()
    pixie = Horse("Pixie", 6, "Arabian")
    pixie.speak()