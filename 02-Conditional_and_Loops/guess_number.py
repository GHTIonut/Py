import random

float_number = random.random() * 10
to_be_guessed = float_number.__round__()
print(to_be_guessed)
user_number = int(input('Guess the number from 0 to 10: '))
k = 0
t = 3
while user_number != to_be_guessed:
    t -= 1
    k += 1
    if t == 0:
        print(f"{t} chances left. Good Bye!")
        break
    print("Try again!")
    print(f"You've tried {k} times. {t} chances left.")
    user_number = int(input("Guess the number from 0 to 10: "))

if user_number == to_be_guessed:
    print("You found the number. Congratulations!")
