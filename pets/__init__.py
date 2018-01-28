# -*- coding: utf-8 -*-

import importlib
import sys

def _list_pet_classes():
    from os.path import dirname, basename, isfile
    import glob
    pyfiles = glob.glob(dirname(__file__)+"/*.py")
    classnames = [ basename(f)[:-3] for f in pyfiles if isfile(f) and not f.endswith('__init__.py')]
    classnames.remove("pet")
    return ["pet"] + classnames   # make sure Pet class is imported first

def _import_one(classname):
    module = sys.modules[__name__]
    submodule = importlib.import_module("pets.{}".format(classname))
    clas = getattr(submodule, classname.capitalize())
    setattr(module, classname.capitalize(), clas)
    module.__dict__.pop(classname,None)
    return clas

Pet   = _import_one("pet")
Cat   = _import_one("cat")
Dog   = _import_one("dog")
Horse = _import_one("horse")

del sys
del importlib
