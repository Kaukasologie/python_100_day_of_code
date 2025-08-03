# Text quest with maximum three possible choices

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

# First choice
user_choice = input('Type "left" or "right"\n').lower()

if user_choice == "right":
    print("Fall into a hole.\nGame Over.")
elif user_choice == "left":
    print("You\'ve come to a lake. There is an island in the middle of the lake.")

    # Second choice
    user_choice = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if user_choice == "swim":
        print("Attacked by trout.\nGame Over.")
    elif user_choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors:\none red, one yellow and one blue.")

        # Third choice
        user_choice = input("Which colour do you choose?\n").lower()
        if user_choice == "red":
            print("It's a room full of fire.\nGame Over.")
        elif user_choice == "blue":
            print("You enter a room of beasts.\nGame Over.")
        elif user_choice == "yellow":
            print("You found the treasure!\nYou Win!")
        else:
            print("There is no door of this color.\nGame Over.")

    else:
        print("Incorrect input. Please restart the game.")

else:
    print("Incorrect input. Please restart the game.")
