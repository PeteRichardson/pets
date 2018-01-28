""" pets module - classes to represent types of pets (e.g. pets.Horse, pets.Cat, etc)

    Each pet has a name, species, age and breed, as well as the ability to speak()

        >>> import pets
        >>> kitty = pets.Cat(name="Bella", age=3, breed="American Shorthair")
        >>> kitty.speak()
        Bella the cat says 'Meow!'
        >>> kitty.json
        '{"age": 3, "breed": "American Shorthair", "name": "Bella", "species": "Cat"}'
"""
# -*- coding: utf-8 -*-

def _pet_classnames():
    """ Finds Pet subclasses in the current folder.

        Assumes each class name is capitalized and each class file is lowercase
        (e.g. horse.py defines class Horse) """
    from os.path import dirname, basename, isfile
    import glob
    pyfiles = glob.glob(dirname(__file__)+"/*.py")
    # Build a list of all classnames (capitalized).  Includes "Pet"
    classnames = [ basename(f)[:-3].capitalize() for f in pyfiles if isfile(f) 
                                             and not f.endswith('__init__.py')]
    # Must import Pet first, so remove it and add it to the front of the list
    classnames.remove("Pet")
    return ["Pet"] + classnames   # make sure Pet class is imported first

def _import(classnames):
    """ import the specified Pet subclasses"""
    import importlib
    import sys
    for classname in classnames:
        module = sys.modules[__name__]
        
        # Load the class and make it visible as an attribute of pets
        submodule = importlib.import_module("pets."+classname.lower())
        setattr(module, classname, getattr(submodule, classname))

        # Specify which classes to export when importing *
        module.__all__.append(classname)
        
        # remove unneeded pets submodule from namespace (e.g. pets.horse)
        module.__dict__.pop(classname.lower(),None)
        

__all__ = []    # classnames are added to this inside _import()
_import( _pet_classnames() )
