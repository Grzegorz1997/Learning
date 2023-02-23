import random
from art import logo
from replit import clear

def pick_number():
    """Randomly pick a number from 1 to 100"""
    number = random.randrange(1,101)
    return number

def take_guess():
    """Validates given user input"""
    ask_over = False
    while not ask_over:
        try:
            guess = int(input("Guess a number from 1 to 100: "))
            if guess in range(1,101):
                ask_over = True
                return guess
            else:
                print("You should pick from 1 to 100, try again")
        except ValueError:
            print("No... input must be an integer. Pick from 1 to 100.")
    
def define_dificulty():
    """"Returns number of guesses based on difficulty level"""
    choices = ["easy","medium","high"]
    ask_over = False
    while not ask_over:
        choice = input("Choose dicifulty level from: easy, medium or high: ")
        choice = choice.lower()
        if choice in choices:
            ask_over = True
            if choice == "easy":
                return 10
            elif choice == "medium":
                return 7
            else:
                return 5
        else:
            print("Incorrect dificulty level, try again.")

        

def result(number, guess):
    """"Compare user guess with picked number"""
    if guess == number:
        return "You guessed right!"
    elif guess > number:
        return "Too high"
    else:
        return "Too low"


    
def play_game():
    print(logo)
    print("Hello!\nWelcome to the number guessing game!\nI'm thinking about a number between 1 and 100.")
    number_of_guesses = define_dificulty()
    print(f"You have {number_of_guesses} guesses.")
    correct_guess = pick_number()
    user_guess = take_guess()
    game_over = False
    
    while not game_over:
        # print(correct_guess) # for testing purpose
        print(result(correct_guess,user_guess))
        if number_of_guesses == 1:
            game_over = True
        else:   
            if user_guess != correct_guess:
                number_of_guesses -=1
                print(f"You have {number_of_guesses} guesses left.")
                user_guess = take_guess()
            else:
                game_over = True
                print("end of the game")
                print("LOLOLO")

play_game()
                   
while input("Do you want to play again? write 'y' or 'n': ") == "y":
    clear()
    play_game()
        
