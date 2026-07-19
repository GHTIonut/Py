queue = []

def add_document(device, document_name):
    intrare = (device, document_name)
    queue.append(intrare)

def print_document():
    removed_item = queue.pop(0)
    print(f"From {removed_item[0]} {removed_item[1]} was printed.")
    
device = str(input("De pe ce tip de device incarci documentul: "))
document = str(input("Numele documentului: "))

add_document(device, document)


print_document()
print(f"Ramase in coada {queue}")
