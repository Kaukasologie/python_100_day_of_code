import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

def generate_phonetic():
    users_word = input("Enter a word: ").upper()
    try:
        output_list = [nato_alphabet_dict[letter] for letter in users_word if letter != " "]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
