from customer import Customer
from coffee import Coffee
from order import Order

if __name__ == "__main__":
    # Create instances
    alice = Customer("Alice")
    latte = Coffee("Latte")
    order1 = Order(alice, latte, 4.5)
    
    # Test relationships
    print(f"{alice.name}'s orders: {len(alice.orders())}")
    print(f"{latte.name} average price: {latte.average_price()}")