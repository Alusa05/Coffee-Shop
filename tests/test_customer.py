from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_init():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_orders():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    assert order in customer.orders()

def test_customer_coffees():
    customer = Customer("Charlie")
    coffee1 = Coffee("Mocha")
    coffee2 = Coffee("Espresso")
    Order(customer, coffee1, 4.5)
    Order(customer, coffee2, 3.5)
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()