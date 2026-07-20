clients = [
    {"name": "Cristian", "spending": 75000},
    {"name": "Johnny", "spending": 120000},
    {"name": "Danny", "spending": 150000},
    {"name": "Andy", "spending": 25000}
]

vip_customers = list(filter(lambda x: x["spending"] > 100000, clients))
print(vip_customers)
for e in vip_customers:
    print(f"Client {e["name"]} is VIP. Total spent: {e["spending"]}")