from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_init():
    coffee = Coffee("Cappuccino")
    assert coffee.name == "Cappuccino"

def test_coffee_orders():
    coffee = Coffee("Americano")
    customer = Customer("Dave")
    order = Order(customer, coffee, 2.5)
    assert order in coffee.orders()

def test_coffee_customers():
    coffee = Coffee("Flat White")
    customer1 = Customer("Eve")
    customer2 = Customer("Frank")
    Order(customer1, coffee, 3.0)
    Order(customer2, coffee, 3.5)
    assert customer1 in coffee.customers()
    assert customer2 in coffee.customers()

def test_coffee_num_orders():
    coffee = Coffee("Macchiato")
    assert coffee.num_orders() == 0
    customer = Customer("Grace")
    Order(customer, coffee, 4.0)
    assert coffee.num_orders() == 1