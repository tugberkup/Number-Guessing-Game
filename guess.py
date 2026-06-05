import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess (1-100): "))

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")

    attempts = attempts + 1

    if guess < number:
        print("Guess Bigger")
    elif guess > number:
        print("Guess Smaller")
    else:
        print(f"Your guess is true! Attempts: {attempts}")
        break