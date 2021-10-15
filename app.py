import commands as cmd

from services.customers import create_customer, list_customers
from services.fakes import seeder
from services.products import create_product, list_products
from services.sales import create_sale, financial, list_sales

run = True

while run:

    command = input('>> ')

    if command == cmd.CMD_EXIT:
        run = False

    if command == cmd.CMD_CREATE_CUSTOMER:
        name = input('Nome: ')
        age = int(input('Idade: '))
        email = input('Email: ')
        create_customer(name, age, email)
    
    if command == cmd.CMD_LIST_CUSTOMER:
        list_customers()
    
    if command == cmd.CMD_CREATE_PRODUCT:
        name = input('Nome: ')
        price = float(input('Preço: '))
        create_product(name, price)
    
    if command == cmd.CMD_LIST_PRODUCT:
        list_products()

    if command == cmd.CMD_CREATE_SALE:
        customer_index = int(input('Cliente: '))
        product_indexs = input('Produtos: ').split(',')
        product_data = [int(i) for i in product_indexs]
        create_sale(customer_index, product_data)
    
    if command == cmd.CMD_LIST_SALE:
        list_sales()
    
    if command == cmd.CMD_VIEW_SALE:
        financial()
    
    if command == 'seed':
        seeder()