import random
from game_data import data
from art import game_logo, vs_logo
from replit import clear

def pick_person():
    pick = random.choice(data)
    followers = int(pick['follower_count'])
    return f"{pick['name']}, {pick['description']} from {pick['country']}", followers

    
def game():
    print(f"{game_logo}\n\n")
    game_over = False
    first_pick,first_value = pick_person()
    first_message = f"Compare A: {first_pick}"
    score = 0
    while not game_over:
        second_pick,second_value = pick_person()
        second_message = f"Against B: {second_pick}"
        correct_bet = max(first_value,second_value)
        if correct_bet == first_value:
            correct_pick = first_pick
        else:
            correct_pick = second_pick

        user_options = {"A":first_value,
            "B": second_value}
        print(first_message)
        print(f"\n\n {vs_logo}\n\n")
        print(second_message)
        ask_over = False
        while not ask_over:
            user_input = input("\nWho has more followers: 'A' or 'B': ").upper()
            if user_input in user_options:
                user_bet = user_options[user_input]
                ask_over = True
                if user_bet != correct_bet:
                    print(f"\nNot correct! Your final score is {score}\n\n")
                    game_over = True
                    
                else:
                    first_pick = correct_pick
                    score += 1
                    print(f"\ncorrect, Your current score is: {score}\n\n")
            else:
                print("\nIncorrect input, try again.")
game()

while input("Do You want to play again? write 'Y' or 'N': ").upper() == "Y":
    clear()
    game()