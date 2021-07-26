"""A number-guessing game."""
#print("I did it!")
# Put your code here
from random import randint
def computer_plays():
    while True:
        try:
            player_num = int(input("Enter your secret number between 1 and 100: "))
            if player_num >= 1 and player_num <=100:
                break
            
        except ValueError:
            print("Oops. That was not a number.")
    

    guess_range_start = 1
    guess_range_end = 100
    while True:
        go = input("Press 'Enter' to see my guess.")
        
        if not go:
            computer_guess = randint(guess_range_start, guess_range_end)
            print(computer_guess)
            if computer_guess > player_num:
                guess_range_end = computer_guess - 1
            elif computer_guess < player_num:
                guess_range_start = computer_guess + 1
            else:
                if computer_guess == player_num:
                    print("I won! That was fun!")
                    break
    

def play(rand_int, player, range_begin, range_end):
    num_of_guesses = 0
    while True:
        try:
            guess = int(input("Your guess? "))
        

            if guess < range_begin or guess > range_end:
                print(f"Guess between {range_begin} and {range_end}.")
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
    guesses_list = []
    while True:
        print("Option A: Guess my number")
        print("Option B: I guess your number") 
        who_plays = input("Enter A or B: ").upper().strip()
        if who_plays == 'B':
            computer_plays()

        else:
            while True:
                try:
                    start = int(input("Choose your number range. Enter the start of range: "))
                    end = int(input("Enter the end of range: "))
                    break
                except ValueError:
                    print("Oops. That was not a number. Please enter a number.")
    
            print(f"{name}, I'm thinking of a number between {start} and {end}.")
            print("Try to guess my number in 8 or fewer guesses.")

            secret_num = randint(start, end)
            outcome = play(secret_num, name, start, end)
            if outcome != 'fail':
                guesses_list.append(outcome)

            if guesses_list != []:

                print(f"Your best game so far was {min(guesses_list)} guesses.")
        play_again = input("Would you like to play again? Y or N: ").upper()
        if 'N' in play_again:
            print("Goodbye.")
            break

main_play()


        
