while True:
    products_count = int(input("Introduceti numarul de produse: "))
    
    if products_count < 1 or products_count > 50:
        print("Numar de produse invalid: ")
        continue
    
    order_price = int(input("Introduceti pretul comenzii: "))

    if order_price <= 0:
        print("Pretul comenzii este invalid: ")
        continue
    
    order_status = int(input("Status plata: \n 0 = Platit \n 1 = In asteptare \n 2 = Neplatit \n"))
    
    if order_status == 0:
        print(f"Comanda valida. \n Numar de produse: {products_count} \n Pretul comenzii: {order_price} \n Status plata: {order_status}")
        break
    elif order_status == 1 or order_status == 2:
        print("Comanda invalida.")
    else:
        print("Index necunoscut pentru valoarea status-ului")
