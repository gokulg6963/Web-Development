import random

num = random.randint(1,9)
guess = int(input("Guess the number: "))


if (num < guess):
    print("Guessed too high")
elif (num > guess):
    print("Guessed too low!")
else:
    print("Ya, you guessed right!")