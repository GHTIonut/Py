clients_list = []
monday_clients = int(input("Clients on monday: "))
clients_list.append(monday_clients)
tuesday_clients = int(input("Clients on tuesday: "))
clients_list.append(tuesday_clients)
wednesday_clients = int(input("Clients on wednesday: "))
clients_list.append(wednesday_clients)
thursday_clients = int(input("Clients on thursday: "))
clients_list.append(thursday_clients)
friday_clients = int(input("Clients on friday: "))
clients_list.append(friday_clients)
saturday_clients = int(input("Clients on saturday: "))
clients_list.append(saturday_clients)
sunday_clients = int(input("Clients on sunday: "))
clients_list.append(sunday_clients)

# Total number of clients:
k = 0
for no_clients in clients_list:
    k += no_clients
print(f'Total number of clients is {k}.')


# Total number of clients from monday to friday:
kk = 0
for no_clients in clients_list[:5]:
    kk += no_clients
print(f'Monday to friday clients number is {kk}.')

# Total number of clients in weekend:
kkk = 0
for no_clients in clients_list[5:]:
    kkk += no_clients
print(f'Weekend number of clients is {kkk}.')

# Check if sunday were more clients than saturday:
if sunday_clients > saturday_clients:
    print(f'On sunday were more clients than saturday.')
elif saturday_clients > sunday_clients:
    print(f"On saturday were more clients than sunday.")
else:
    print("Sunday and saturday has exactly the same number of clients")

# Check if clients in work days were more than in weekend:
work_days = sum(clients_list[:5])
weekend_days = sum(clients_list[5:])
if work_days > weekend_days:
    print("On work days were more clients than weekend days.")
elif weekend_days > work_days:
    print("On weekend days were more clients than work days.")
else:
    print("Work days and weekend days has exactly the same number of clients.")

# Check if the week was successful:
if work_days + weekend_days > 1000 or weekend_days > 500:
    print("Successful week.")
else:
    print("Not so good week.")