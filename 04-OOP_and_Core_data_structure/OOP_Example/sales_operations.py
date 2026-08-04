def total_sales(sales):
    return sum(sales.values())

def most_sold_product(sales):
    return max(sales.items(), key=lambda item: item[1])

def least_sold_product(sales):
    return min(sales.items(), key=lambda item: item[1])

def get_product_sales(sales, product):
    try:
        return sales[product]
    except KeyError:
        return f"Produsul '{product}' nu exista"
    
def validates_sales_data(sales):
    errors = []
    
    for product, quantity in sales.items():
        if not isinstance(quantity, int):
            errors.append(f"{product}: cantitatea trebuie sa fie un numar intreg.")
        elif quantity < 0:
            errors.append(f"{product}: cantitatea nu poate fi negativa.")
        elif quantity > 999999:
            errors.append(f"{product}: cantitate suspect de mare.")
            
    return errors

def critical_stocks(sales, limit):
    return list(filter(lambda item: item[1] < limit, sales.items()))
