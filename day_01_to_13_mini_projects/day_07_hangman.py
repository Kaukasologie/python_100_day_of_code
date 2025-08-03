import random
from day_07_hangman_art_and_words import logo, stages, word_list

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = "_" * len(chosen_word)
print("Word to guess: " + placeholder)

placeholder = list(placeholder)
lives = 6
correct_letters = []
game_over = False

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    # Shows the letter if it is guessed or is in the list of guessed letters, otherwise shows an underscore
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # All letters are guessed
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
