from copy import deepcopy


class Prototype:

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Registers the object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Deletes an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clones an object"""
        obj = deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj