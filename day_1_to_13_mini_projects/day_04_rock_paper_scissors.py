import random

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# 0 = rock, 1 = paper, 2 = scissors
hand_choice = [rock, paper, scissors]

print("Let's play rock, paper, scissors game!\n")
print("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.")

user_choice = int(input("--->> "))
computer_choice = random.randint(0, 2)



if 0 <= user_choice < 3:
    print(f"You chose: \n{hand_choice[user_choice]}")
    print(f"Computer chose: \n{hand_choice[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice < computer_choice:
        print("You lose!")
    elif user_choice == computer_choice:
        print("It's a draw!")

else:
    print("You typed an invalid number. Please restart the game.")
