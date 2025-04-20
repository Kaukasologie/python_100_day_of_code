# Test: start hand - [11, 2](13) add ace[1](14) and add 8 = 12 [1, 2, 1, 8]

import random


logo = (r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
print(logo)

def add_card_to_list(hand):
    """Take a list of cards and return the new list with added card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    if sum(hand) + card > 21:
        if card == 11:
            card = 1
        else:
            for i in range(len(hand)): # option - if 11 in hand: hand.remove(11), hand.append(1) - but order will wrong
                if hand[i] == 11:
                    hand[i] = 1
    hand.append(card)
    return hand

def blackjack_check(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return True
    else:
        return False

def play_game():
    user_hand = []
    computer_hand = []
    for _ in range(2):
        add_card_to_list(user_hand)
        add_card_to_list(computer_hand)

    game_over = False

    while not game_over:
        print(f"\nYour cards: {user_hand}, current score: {sum(user_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")
        if blackjack_check(computer_hand):
            game_over = True
        elif blackjack_check(user_hand):
            game_over = True
        elif sum(user_hand) > 21:
            game_over = True
        elif input("\nType 'y' to get another card, type 'n' to pass: ").lower() == "y":
            add_card_to_list(user_hand)
        else:
            game_over = True
            while sum(computer_hand) < 17:
                add_card_to_list(computer_hand)

    print(f"\nYour final hand: {user_hand}, final score: {sum(user_hand)}")
    print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}\n")

    if blackjack_check(computer_hand):
        print("Lose, opponent has Blackjack 😱")
    elif blackjack_check(user_hand):
        print("Win with a Blackjack 😎")
    elif sum(user_hand) > 21:
        print("You went over. You lose 😭")
    elif sum(computer_hand) > 21:
        print("Opponent went over. You win 😁")
    elif sum(user_hand) == sum(computer_hand):
        print("Draw 🙃")
    elif sum(user_hand) > sum(computer_hand):
        print("You win 😃")
    else:
        print("You lose 😤")

while input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 3)
    print(logo)
    play_game()
