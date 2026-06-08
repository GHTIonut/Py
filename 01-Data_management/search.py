import csv

with open("sales.csv", "r", encoding="utf-8") as file:
    
    reader = csv.reader(file)
    header = next(reader)
    search = input("Search: ").strip().lower()

    # Solution no.1 
    # Finds the list that contains user's input.
    
    for row in reader:
        for cell in row:
            if search in cell:
                print(row)
            
    # Solution no.2:
    
    # for row in reader:
    #     if any(search in cell for cell in row):
    #          print(row)
