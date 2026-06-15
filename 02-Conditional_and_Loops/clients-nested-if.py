regular_client = ['Mark', 'John', 'Tiffany']
loyal_client = ['Daniel', 'Torben', 'Frank']

client_name = input("Client name: ")
if client_name in regular_client:
    print('This client is regular.')
    sum_spent = int(input('Sum spent is: '))
    if sum_spent < 100:
        print('Discount not applicable.')
    if sum_spent >= 100 and sum_spent <= 500:
        print(f"5% percent discount.")
    if sum_spent > 500:
        print(f"10% discount.")
elif client_name in loyal_client:
    print('This client is loyal.')
    sum_spent = int(input("Sum spent is: "))
    if sum_spent < 100:
        print(f"5% percent discount.")
    if sum_spent >= 100 and sum_spent <= 500:
        print(f"10% percent discount.")
    if sum_spent > 500:
        print(f"15% percent discount.")
else:
    print('This person is not our client.')