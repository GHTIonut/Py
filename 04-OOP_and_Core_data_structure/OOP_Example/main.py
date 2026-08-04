from sales_operations import (
    total_sales,
    most_sold_product,
    least_sold_product,
    get_product_sales,
    validates_sales_data, 
    critical_stocks
)

sales = {
    "TV": 40, 
    "Phones": 70, 
    "Laptop": 80, 
    "Fridge": 100
}

print(f"Total produse vandute: ", total_sales(sales))
print(f"Cele mai vandute produse: ", most_sold_product(sales))
print(f"Cele mai putin vandute produse: ", least_sold_product(sales))
print(f"Vanzari laptop: ", get_product_sales(sales, "Laptop"))
print(f"Vanzari TV: ", get_product_sales(sales, "TV"))

errors = validates_sales_data(sales)

if errors:
    print("Erori gasite: ")
    for error in errors:
        print(error)
else:
    print("Date valide.")
    
print(f"Produse cu stoc critic: ")
print(critical_stocks(sales, 75))