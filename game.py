"""A number-guessing game."""
#print("I did it!")
# Put your code here
from random import randint

secret_num = randint(1,101)

name = input("Howdy! What is your name: ").title()
print(f"{name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")

num_of_guesses = 0

while True:
    try:
        guess = int(input("Your guess? "))
    

        if guess < 1 or guess > 100:
            print("Guess between 1 and 100.")
        else:
            num_of_guesses += 1
            if guess > secret_num:
                print("Your guess is too high -- try again.")
            elif guess < secret_num:
                print("Your guess is too low -- try again.")
            else:
                print(f"Well done, {name}! You found my number in {num_of_guesses} tries!")
                break 
    except ValueError:
        print("Oops! The was not a number. Try again.")   