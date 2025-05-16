class Coffee:
    # A class variable to track all the coffee instances
    all = []

    def __init__(self,name):
        self.name = name
        Coffee.all.append(self)