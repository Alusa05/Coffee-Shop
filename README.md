# Project Overview
This project is known as Coffee Shop. It implements a coffee shop domain with three models:
 Coffee - Represents the varieties of coffees available
 Customer - Represents the shop customers
 Order - Connecting customers to the coffees they have ordered/purchased
The system maintains a many-to-many relationship between the coffee and customer through the order model

# Project Author
This project has been implemented by Lisa Alusa

# Installation / How to use
1. Clone the repository:
git clone: git@github.com:Alusa05/Coffee-Shop.git
cd Coffee-Shop

2. Set up a python environment:
pipenv install
pipenv shell

# Project Structure
Coffee-shop/
├── Pipfile
├── debug.py            # Manual testing script
├── customer.py         # Customer model
├── coffee.py           # Coffee model
├── order.py            # Order model
└── tests/
    ├── test_customer.py
    ├── test_coffee.py
    └── test_order.py

# Testing
Run all tests:
python -m pytest tests/

# License 
Distributed under the MIT License

# Contact
Email - lisa.sayi@student.moringaschool.com
Project link - https://github.com/Alusa05/Coffee-Shop