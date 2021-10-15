from database import sales, customers, products
from models.sale import Sale

def create_sale(customer_index, product_indexs):
    customer = customers[customer_index]
    products_data = [products[i] for i in product_indexs]
    sale = Sale(customer, products_data)
    sales.append(sale)

def list_sales():
    for sale in sales:
        print('------')
        print(sale.customer.name)
        for product in sale.products:
            print(product.name)
        print('------')

def financial():
    total = 0
    for sale in sales:
        total += sale.total()
    print('Total: ', total)
