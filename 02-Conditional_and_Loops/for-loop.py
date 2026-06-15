prices = {
    'Eggs': 0.50,
    'Cheese': 4.65,
    'Bread': 2.40,
    'Yogurt': 1.75
}

items_price = []
total = 0

for price in prices.values():
    print(price)
    items_price.append(price)
    print(items_price)
    total += price
    print(total)
        
