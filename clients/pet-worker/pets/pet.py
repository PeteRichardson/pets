# -*- coding: utf-8 -*-

from random import choice, randrange
import json 
import pdb

class InvalidPetData(ValueError):
    pass

class Pet(object):
    species = None   # Generic Pet has no species

    subclass_names = None

    def __init__(self, species=None, name=None, age=None, breed=None):
        Pet.subclass_names = Pet.subclass_names or [clas.__name__ for clas in Pet.__subclasses__()]
        if species not in Pet.subclass_names:
            raise TypeError("You can't instantiate a Pet directly.  Instantiate one of {}".format(Pet.subclass_names))

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

        if not (0 < self.age < 25):
            raise ValueError("Invalid age... {}. Expected 0 < age < 25.".format(self.age))

    @property
    def sound(self):
        pass

    def speak(self):
        print("{} the {} says '{}!'".format(self.name, self.species.lower(), self.sound))

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return json.dumps(self.__dict__)

    @property
    def json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def  from_json(cls, jsonstr):
        try:
            import pdb
            #pdb.set_trace()
            data = json.loads(jsonstr)
            speciesname = data.pop('species') # Figure out the species (i.e. the class)   
            clas = globals()[speciesname]     # Lookup the class
            obj= clas(**data)                 # Create an object of that type and fill in data
            return obj
        except KeyError as e:
            raise InvalidPetData("pet needs a species")

    @classmethod
    def random(cls):
        subs = cls.__subclasses__()
        if subs:
            return choice(subs)()
        else:
            return cls()


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
