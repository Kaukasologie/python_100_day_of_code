# I didn't know about the condition with aces until this happened in a game on the website:
# At first I had an ace (11 points) and a deuce (2 points). I got an ace (11 points).
# The total should have been 24 points (11+2+11), but it became 14 points, since one of the aces turned into 1.
# Then I got another eight (8 points) and the total should have been 22 (11+2+1+8), but now the second ace became 1
# and the score became 12 points (1+2+1+8).

# TODO: Add conditions for ace

import random


print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_card():
    return random.choice(cards)


quit_game = False

while not quit_game:
    if input("\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() != 'y':
        quit_game = True
    else:
        your_hand = [pick_card(), pick_card()]
        computer_hand = [pick_card()]
        game_over = False
        blackjack = False

        if sum(your_hand) == 21:
            blackjack = True
        else:
            while not game_over:
                print(f"\nYour cards: {your_hand}, current score: {sum(your_hand)}")
                print(f"Computer's first card: {computer_hand}")
                if sum(your_hand) > 21:
                    game_over = True
                elif input("\nType 'y' to get another card, type 'n' to pass: ").lower() == "y":
                    your_hand.append(pick_card())
                else:
                    game_over = True
                    while sum(computer_hand) < 17:
                        computer_hand.append(pick_card())

        print(f"\nYour final hand: {your_hand}, final score: {sum(your_hand)}")
        print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}\n")

        if blackjack:
            print("Win with a Blackjack 😎")
        elif sum(your_hand) > 21:
            print("You went over. You lose 😭")
        elif sum(your_hand) < sum(computer_hand):
            if sum(computer_hand) > 21:
                print("Opponent went over. You win 😁")
            elif sum(computer_hand) == 21 and len(computer_hand) == 2:
                print("Lose, opponent has Blackjack 😱")
            else:
                print("You lose 😤")
        elif sum(your_hand) > sum(computer_hand):
            print("You win 😃")
        else:
            print("Draw 🙃")
