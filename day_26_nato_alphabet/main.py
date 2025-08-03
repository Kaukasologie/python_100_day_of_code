import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

users_word = input("Enter a word: ").upper()

# output_list = [nato_alphabet_dict[letter] for letter in users_word] - doesn't work with spaces

for letter in users_word:
    if letter == " ":
        print()
    else:
        for (key, value) in nato_alphabet_dict.items():
            if letter == key:
                print(key, value)

