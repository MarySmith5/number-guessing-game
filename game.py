"""A number-guessing game."""
#print("I did it!")
# Put your code here
from random import randint


name = input("Howdy! What is your name: ").title()
print(f"{name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")
guesses_list = []

while True:

    secret_num = randint(1,100)


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
                    guesses_list.append(num_of_guesses)
                    break 
        except ValueError:
            print("Oops! The was not a number. Try again.")

    print(f"Good game! Your best game so far was {min(guesses_list)} guesses.")
    play_again = input("Would you like to play again? Y or N: ").upper()
    if 'N' in play_again:
        print("Goodbye.")
        break
    
