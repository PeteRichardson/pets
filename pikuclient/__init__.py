""" pikuclient - client side module for piku api """

from pets import *

__all__ = ["Pet"] + [clas.__name__ for clas in Pet.__subclasses__()]



