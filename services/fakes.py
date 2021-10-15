from faker import Faker
from random import randint, choice

from database import customers, products, sales
from models.customer import Customer
from models.product import Product
from models.sale import Sale

fake = Faker('pt_BR')

quantity = 100

def seeder():

    for _ in range(quantity):
        customer = Customer(
            fake.name(),
            randint(8, 99),
            fake.email()
        )
        customers.append(customer)

        product = Product(
            fake.company(),
            randint(1, 100)
        )
        products.append(product)

    for _ in range(quantity):
        products_data = []
        quantity_products = randint(1,10)
        for _ in range(quantity_products):
            index = randint(0, 10)
            p = products[index]
            products_data.append(p)

        sale = Sale(
            choice(customers),
            products_data
        )
        sales.append(sale)