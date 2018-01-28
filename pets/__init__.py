# -*- coding: utf-8 -*-

import importlib

def _list_pet_classes():
    from os.path import dirname, basename, isfile
    import glob
    pyfiles = glob.glob(dirname(__file__)+"/*.py")
    classnames = [ basename(f)[:-3] for f in pyfiles if isfile(f) and not f.endswith('__init__.py')]
    classnames.remove("pet")
    #return ["pet"] + classnames   # make sure Pet class is imported first
    return ["pet","horse"]

def import_one(classname):
    if classname == 'pet':
        print "importing {}".format(classname)
        submodule = "pets.{}".format(classname)
        print "submodule = {}".format(submodule)
        m = importlib.import_module(submodule,classname)
        print "m = {}".format(m)
        actualpetclass = getattr(m,classname.capitalize())
        print "actualpetclass = {}".format(actualpetclass)
        setattr(module, classname.capitalize(), actualpetclass)
        print dir(module)
    else:
        print "importing {}".format(classname)
        submodule = "pets.{}".format(classname)
        print "submodule = {}".format(submodule)
        m = importlib.import_module(submodule,classname)
        print "m = {}".format(m)
        actualpetclass = getattr(m,classname.capitalize())
        print "actualpetclass = {}".format(actualpetclass)
        setattr(module, classname.capitalize(), actualpetclass)
        print dir(module)
 
import sys

module = sys.modules[__name__]  # pets module
submodule = importlib.import_module("pets.pet", "pet") # pets.pet module
clas = getattr(submodule, "Pet")  # pets.pet.Pet class
setattr(module, "Pet", clas)
Pet = clas

submodule = importlib.import_module("pets.cat") # pets.pet module
clas = getattr(submodule, "Cat")  # pets.pet.Pet class
setattr(module, "Cat", clas)
Cat = clas

submodule = importlib.import_module("pets.dog") # pets.pet module
clas = getattr(submodule, "Dog")  # pets.pet.Pet class
setattr(module, "Dog", clas)
Dog = clas

submodule = importlib.import_module("pets.horse") # pets.pet module
clas = getattr(submodule, "Horse")  # pets.pet.Pet class
setattr(module, "Horse", clas)
Horse = clas