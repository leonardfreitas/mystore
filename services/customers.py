from database import customers
from models.customer import Customer

def create_customer(name, age, email):
    customer = Customer(name, age, email)
    customers.append(customer)

def list_customers():
    for customer in customers:
        print(customer)
