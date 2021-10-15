class Sale:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    def total(self):
        t = 0
        for product in self.products:
            t += product.price
        return t
