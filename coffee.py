class Coffee:
    # A class variable to track all the coffee instances
    all = []

    def __init__(self,name):
        self.name = name
        Coffee.all.append(self)

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self,value):
            if not isinstance(value, str):
                raise TypeError("Name must be a string")
            if len(value) < 3:
                raise ValueError("Name must be at least 3 characters long")
            if hasattr(self, '_name'):
                raise AttributeError("Name has already been set")
            raise AttributeError(" Coffee name cannot be changed")
        self._name = value

        def orders(self):
            return [order for order in Order.all if order.customer == self]
        
        def coffees(self):
            return list ({order.coffee for order in self.orders()})
        
        def create_order(self,coffee,price):
            return Order(self, coffee, price)

