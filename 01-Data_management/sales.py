import csv

with open("sales.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader) 
    rows = list(reader)
    print(len(rows[0]))
    print(rows[0])
    
    column_to_find = input('Column name to be displayed: ')
    for column in header:
        if column == column_to_find:
            index_column = header.index(column_to_find)
            print(index_column)
            print(f'The column {column} exists.')
            for i in range(len(rows)):
                print(rows[i][index_column]) 

                

        
        
    
    
    

