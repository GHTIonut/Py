products = [
    {"name": "Laptop", "price": 85000, "discount": True},
    {"name": "Phone", "price": 50000, "discount": False},
    {"name": "TV", "price": 60000, "discount": True},
    {"name": "Camera", "price": 25000, "discount": False},
]

discounted_products = list(filter(lambda x: x["discount"] == True, products))
print(discounted_products)

for p in discounted_products:
    print(f"{p["name"] } is on discount and its price is {p['price']}.")
