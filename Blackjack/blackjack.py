import random
from replit import clear
from art import logo

def deal_card():
    """"Returns random card from the deck"""
    cards = [11, 1, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list):
    """"Take the list of Cards, checks for Blackjack and replaces Ace for 1 if over 21. Finally return Score """
    score = sum(list)
    if score == 21 and len(list) == 2:
        score = 0
    if 11 in list and score >21:
        list.remove(11)
        list.append(1)
    return score

    
def compare(user, computer):
    """Compares user score and computer score"""
    if user == computer:
        return "It's a draw"
    elif computer == 0:
        return "You Lost by blackjack"
    elif user == 0:
        return "You won by blackjack"
    elif user > 21:
        return "You went over, You lost"
    elif computer >21:
        return "computer went over, You won"
    elif user > computer:
        return "You win"
    else:
        return "You lost"

def play_game():
    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards are {user_cards}, Your score is {user_score} \nComputer first card is {computer_cards[0]}")
        if user_score == 0 or computer_score ==0 or user_score >21:
            game_over = True
        else:
            if input("Do You want to add another card? type 'y' or 'n': ") =="y":
                user_cards.append(deal_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards) #check if needed
        

        
    print(f"Your final cards: {user_cards}, Your total Score is {user_score} \nComputer Cards: {computer_cards}")
    print(compare(user_score,computer_score))
    
play_game()

while input("Do You want to play another game? input 'y' or 'n': ") =="y":
    clear()
    print(logo)
    play_game()