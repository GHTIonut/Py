from employee import Employee
from product import Product
from user import User

product1 = Product("TV LG OLED", 3000, 50, "Diagonala 139cm")
product2 = Product("TV LG QLED", 2500, 40, "Diagonala 139cm")
product3 = Product("TV Samsung", 3200, 8, "Diagonala 139cm")
product4 = Product("TV Sony Bravia", 4800, 15, "Diagonala 164cm")
product5 = Product("TV Philips Ambilight", 3700, 5, "Diagonala 121cm")
print(product1.check_quantity()) # True
print(product2.check_quantity()) # True
print(product3.check_quantity()) # False
products = [product1, product2, product3, product4, product5] # Products List

user1 = User(
    "Johnny", "Johnny96", "Johnny96@gmail.com", "+40700123456", "Bucharest, Romania"
)  # Object of User class

print(user1.check_email()) # True
print(user1.shopping_history)  # Output: Empty list
user1.add_product(product1)  # Appends first product
print(user1.total_spent()) # Total spent 3000.0


user2 = User(
    "July", "July99", "July99@gmail.com", "+40700321321", "Zurich, Switzerland"
)  # Object of User class

print(user2.check_email()) # True
print(user2.shopping_history) # Output: Empty list
user2.add_product(product1) # Appends first product
user2.add_product(product2) # Appends second product
print(user2.total_spent()) # Total spent 5500.0

user3 = User(
    "George",
    "GeorgeMistake31",
    "GMistake.yahoo.com",
    "+0123456789",
    "Anywhere, Earth planet",
)  # Object of User class
users = [user1, user2, user3]

print(user3.check_email()) # False

employee1 = Employee("Johnny", "Johnny01@gmail.com", 7800, "Bucharest, Romania")
employee2 = Employee("July", "Johnny96.yahoo.com", 7000, "Zurich, Switzerland")
employees = [employee1, employee2]
print(employee1.check_email()) # True
print(employee2.check_email()) # False

print(employee1.increase_salary(0.05))
print(employee1.salary)
print(employee2.increase_salary(0.10))
print(employee2.salary)
