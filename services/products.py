from database import products
from models.product import Product

def create_product(name, price):
    product = Product(name, price)
    products.append(product)


def list_products():
    for product in products:
        print(product)