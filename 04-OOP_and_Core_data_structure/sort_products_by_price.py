products = [
    {"Name": "Milk", "Price": 5, "Weight": 1},
    {"Name": "Water", "Price": 2, "Weight": 2},
    {"Name": "Sunflower Oil", "Price": 3, "Weight": 1},
    {"Name": "Soda", "Price": 1.5, "Weight": 0.5},
]

products.sort(key=lambda x: x["Price"])

for product in products:
    print(f"{product["Name"]} has the price of {product["Price"]}")