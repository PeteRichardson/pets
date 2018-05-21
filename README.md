# Pets - Simple pet classes with random pet generator

Currently supports cats, dogs and horses.

Pet fields include species, breed, age and name.

random() function on each class generates a random pet of the appropriate species

## Examples:

### Create a Cat

``` python
 >>> from pets import Cat
 >>> mycat = Cat(name="Bella", age=4, breed="American Shorthair")
 >>> mycat.breed
 'American Shorthair'
 >>>
 >>> from pets import Cat
 >>> Cat.random()
 {"age": 15, "breed": "Maine Coon", "name": "Apollo", "species": "Cat"}
 >>>
```

### Generate a random pet (Horse, Dog or Cat)

```
 >>> from pets import Pet
 >>> Pet.random()
 {"age": 19, "breed": "Shih Tzu", "name": "Mr Kitty", "species": "Dog"}
 >>> Pet.random()
 {"age": 18, "breed": "Persian", "name": "Bucko", "species": "Cat"}
 >>>
```