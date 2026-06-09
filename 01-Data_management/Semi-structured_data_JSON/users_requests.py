import requests
import json # used only with solution no.2 

response = requests.get('https://jsonplaceholder.typicode.com/users')
# print (response, type(response))
# print(response.status_code)
if response.status_code == 200:
    # print(response.text)

    # Solution no.1:
    users = response.json() # ==> json() method converts response in native Pyhon objects.

    # Solution no.2 == solution no.1

    # text_response = response.text #
    # print(text_response)
    # users = json.loads(text_response)
    # print(users, type(users))

    for user in users:
        print(f'Name of the user with id {user['id']} is {user['name']}.') 
        print(f'{user['name']} email is {user['email']}.')
        print(f"Or you can call the user at phone no. {user['phone']}.")
        print(f'{user['name']} works for {user['company']['name']}. \n')
        
    for user in users: 
        if (user['id'] % 2 == 0):
            print(f"Even ID: {user['id']}")
            
    print(f"\n")
    
    for user in users:
        if(user['id'] % 2 != 0):
            print(f'Odd ID: {user['id']}')
            
    
            
    
