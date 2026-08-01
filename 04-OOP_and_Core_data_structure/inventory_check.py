sales = {
    "laptop": 15, 
    "mouse": 150, 
    "keyboard": 85, 
    "monitor" :30, 
    "usb cable": 200
    }

# 1. Cantitatea totala de produse vandute:
total_sales = sum(sales.values())
print(total_sales)

# 2. Produsul cel mai vandut:
max_sales = max(sales.items(), key=lambda item: item[1])
print(f"Cel mai vandut produs este {max_sales[0]} cu {max_sales[1]} de unitati vandute.")

# 3. Produsul cel mai putin vandut:
min_sales = min(sales.items(), key=lambda item: item[1])
print(f"Cel mai putin vandut produs este {min_sales[0]} cu {min_sales[1]} de unitati vandute.")

# 4. Este vândut produsul "Web camera"? Dacă nu, adăugați-l în dicționar cu valoarea 0.
if "Web camera" not in sales:
    sales["Web camera"] = 0
print(sales)

# 5. Rectificare numar de unitati vandute pentru monitor.
sales["monitor"] += 5

# Listare dictionar actualizat
print(sales)

# 6. Functie pentru listarea produselor critice:
def critical_products(sales_dict):
    critical = []

    for product, quantity in sales_dict.items():
        if quantity < 50:
            critical.append(product)

    return critical

# 7. Verificați dacă datele din dicționar sunt valide, de exemplu, dacă există un produs care are o cantitate negativă de unități vândute.
valid_data = True

for product, quantity in sales.items():
    if quantity < 0:
        print(f"Eroare: {product} are o cantitate negativă ({quantity}).")
        valid_data = False

if valid_data:
    print("Toate datele sunt valide.")

# 8. Verificare produse critice
print(critical_products(sales))
