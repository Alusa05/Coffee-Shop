class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

@property
def name(self):
    return self._name   

@name.setter
     def name(self, value):
    if not isinstance(value, str):
        raise TypeError("Name must be a string")

