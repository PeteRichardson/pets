# -*- coding: utf-8 -*-

import importlib
import sys

def _list_pet_classes():
    from os.path import dirname, basename, isfile
    import glob
    pyfiles = glob.glob(dirname(__file__)+"/*.py")
    classnames = [ basename(f)[:-3].capitalize() for f in pyfiles if isfile(f) and not f.endswith('__init__.py')]
    classnames.remove("Pet")
    return ["Pet"] + classnames   # make sure Pet class is imported first

def _import_one(classname):
    submodule = importlib.import_module("pets.{}".format(classname.lower()))
    clas = getattr(submodule, classname)
    module = sys.modules[__name__]
    setattr(module, classname, clas)
    module.__dict__.pop(classname.lower(),None)
    #setattr(sys.modules[__name__], classname, clas)
    #sys.modules[__name__].__dict__.pop(classname.lower(),None)
    return clas

for classname in _list_pet_classes():
    _import_one(classname)

del sys
del importlib
del classname
