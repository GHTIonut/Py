from product import Product

class User:

    def __init__(self, name, username, email, phone, address):
        self.name = str(name)
        self.username = str(username)
        self.email = str(email)
        self.phone = str(phone)
        self.address = str(address)
        self.shopping_history = []

    def check_email(self):
        if "@" in self.email:
            return True
        else:
            return False
        
    def add_product(self, product):
        self.shopping_history.append(product)

    def total_spent(self):
        total = 0

        for product in self.shopping_history:
            total += product.price
        return total