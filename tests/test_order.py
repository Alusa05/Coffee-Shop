from order import Order
from customer import Customer
from coffee import Coffee

def test_order_init():
    customer = Customer("Hank")
    coffee = Coffee("Irish Coffee")
    order = Order(customer, coffee, 6.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 6.5

def test_order_price_validation():
    customer = Customer("Ivy")
    coffee = Coffee("Turkish Coffee")
    try:
        Order(customer, coffee, 0.5)
        assert False, "Should raise ValueError"
    except ValueError:
        pass

def test_order_immutable_price():
    customer = Customer("Jack")
    coffee = Coffee("Cold Brew")
    order = Order(customer, coffee, 4.5)
    try:
        order.price = 5.0
        assert False, "Should raise AttributeError"
    except AttributeError:
        pass