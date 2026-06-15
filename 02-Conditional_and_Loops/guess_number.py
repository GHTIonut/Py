import random

float_number = random.random() * 10
int_number = float_number.__round__()
print(int_number)
user_number = int(input('Guess the number from 0 to 10: '))
k = 0
t = 3
while user_number != int_number:
    t -= 1
    k += 1
    if t == 0:
        print(f"{t} chances left. Good Bye!")
        break
    print("Try again!")
    print(f"You've tried {k} times. {t} chances left.")
    user_number = int(input("Guess the number from 0 to 10: "))

if user_number == int_number:
    print("You found the number. Congratulations!")
