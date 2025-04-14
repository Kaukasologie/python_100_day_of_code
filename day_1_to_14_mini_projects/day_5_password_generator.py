import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
password_length = int(input("How long should your password be?\n"))
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_digits = int(input(f"How many numbers would you like?\n"))

total_characters = number_of_letters + number_of_symbols + number_of_digits

# !Bad practice, should be avoided by calculating after each input how many characters are left and showing it to the user
if total_characters > password_length:
    print("\nThe number of characters must not exceed its length.")
elif total_characters < password_length:
    print("\nThe number of characters must not be less than the password length.")

else:
    password = []
    chars_position = []

    # fill out the list for further replacement
    for char in range(password_length):
        password += ' '

    if number_of_letters > 0:
        # Replacing spaces with letters
        for char in range(number_of_letters):
            place = random.randint(0, password_length - 1)

            # Change random position if it was there before
            while place in chars_position:
                place = random.randint(0, password_length - 1)

            # Remember the new place and make a replacement there.
            chars_position.append(place)
            password[place] = random.choice(letters)

    # Repeat the same for the symbols
    if number_of_symbols > 0:
        for char in range(number_of_symbols):
            place = random.randint(0, password_length - 1)
            while place in chars_position:
                place = random.randint(0, password_length - 1)
            chars_position.append(place)
            password[place] = random.choice(symbols)

    # Repeat the same for the digits
    if number_of_digits > 0:
        for char in range(number_of_digits):
            place = random.randint(0, password_length - 1)
            while place in chars_position:
                place = random.randint(0, password_length - 1)
            chars_position.append(place)
            password[place] = random.choice(digits)

    # Make a string from the list
    password = ''.join(password)

    print(f"\nYour password is: {password}")
