sales_data = [
    {"product": "Smartphone", "month": "January", "quantity": 150},
    {"product": "Laptop", "month": "January", "quantity": 80},
    {"product": "Tablet", "month": "January", "quantity": 50},
    {"product": "Smartphone", "month": "February", "quantity": 200},
    {"product": "Laptop", "month": "February", "quantity": 90},
    {"product": "Tablet", "month": "February", "quantity": 60},
    {"product": "Smartphone", "month": "March", "quantity": 250},
    {"product": "Laptop", "month": "March", "quantity": 100},
    {"product": "Tablet", "month": "March", "quantity": 70},
]

# Rezultatele așteptate ale programului:

# Total sales by product:
# - Smartphone: 600 units
# - Laptop: 270 units
# - Tablet: 180 units

# Total sales by month:
# - January: 280 units
# - February: 350 units
# - March: 420 units

smartphone_sales = 0
for item in sales_data:
    if item["product"] == "Smartphone":
        smartphone_sales += item["quantity"]
print(f"Total vanzari smartphone-uri: {smartphone_sales}")

laptop_sales = 0
for item in sales_data:
    if item["product"] == "Laptop":
        laptop_sales += item["quantity"]
print(f"Total vanzari laptop-uri: {laptop_sales}")

tablet_sales = 0
for item in sales_data:
    if item["product"] == "Tablet":
        tablet_sales += item["quantity"]
print(f"Total vanzari tablete: {tablet_sales}")

january_sales = 0
for item in sales_data:
    if item["month"] == "January":
        january_sales += item["quantity"]
print(f"Vanzarile pe luna ianuarie: {january_sales}")

february_sales = 0
for item in sales_data:
    if item["month"] == "February":
        february_sales += item["quantity"]
print(f"Vanzarile pe luna februarie: {february_sales}")

march_sales = 0
for item in sales_data:
    if item["month"] == "March":
        march_sales += item["quantity"]
print(f"Vanzari pe luna martie: {march_sales}")

