"""A number-guessing game."""
#print("I did it!")
# Put your code here
from random import randint
    

def play(rand_int, player):
    num_of_guesses = 0
    while True:
        try:
            guess = int(input("Your guess? "))
        

            if guess < 1 or guess > 100:
                print("Guess between 1 and 100.")
            else:
                num_of_guesses += 1
                if num_of_guesses == 8:
                    print('That was your last guess...')
                    if guess != rand_int:
                        print('Sorry. You failed this round.')
                        return "fail"
                if guess > rand_int:
                    print("Your guess is too high -- try again.")
                elif guess < rand_int:
                    print("Your guess is too low -- try again.")
                else:
                    print(f"Well done, {player}! You found my number in {num_of_guesses} tries!")
                    return num_of_guesses
                    
        except ValueError:
            print("Oops! The was not a number. Try again.")

            
                
    return num_of_guesses


def main_play():

    name = input("Howdy! What is your name: ").title()
    print(f"{name}, I'm thinking of a number between 1 and 100.")
    print("Try to guess my number in 8 or fewer guesses.")
    guesses_list = []

    while True:

        secret_num = randint(1,100)
        outcome = play(secret_num, name)
        if outcome != 'fail':
            guesses_list.append(outcome)

        if guesses_list != []:

            print(f"Your best game so far was {min(guesses_list)} guesses.")
        play_again = input("Would you like to play again? Y or N: ").upper()
        if 'N' in play_again:
            print("Goodbye.")
            break

main_play()


        
