class Product:

    def __init__(self, name, price, quantity, description):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        self.description = str(description)

    def check_quantity(self):
        if self.quantity < 10:
            return False
        else:
            return True


