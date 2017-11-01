# Descriptors - Getters and Setters
class Person:

    def __init__(self):
        self._name = ""

    @property
    def name(self):
        print("Getting {}".format(self._name))
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        print("Setting {}".format(self._name))

    @name.deleter
    def name(self):
        print("Deleting {}".format(self._name))

obj = Person()
obj.name = "Ram"
obj.name
del obj.name
