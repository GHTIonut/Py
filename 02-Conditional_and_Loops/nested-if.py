import re

age = int(input('How old are you: '))
regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{5,}$"

if age > 18:
    password = input('Type your password: ')
    if re.fullmatch(regex, password) :
        print('Well done!')
    else:
        print('Password is Not good.')
else:
    print("End of program. You`re too young.")