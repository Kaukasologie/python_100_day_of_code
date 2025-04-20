# Takes two names and checks if they contain letters from the phrase.
# The number of letters found in the first word ("True") is multiplied by 10.
# The number of letters found in the second word "Love" is added to it.

boy_name = input('Boy name:\n--->> ')
girl_name = input('Girl name:\n--->> ')

def calculate_love_score (name_1, name_2):
    name_1 = name_1.lower()
    name_2 = name_2.lower()
    score = 0

    for letter in "true":
        score = score + name_1.count(letter) + name_2.count(letter)

    score *= 10

    for letter in "love":
        score = score + name_1.count(letter) + name_2.count(letter)

    print(score)

calculate_love_score(boy_name, girl_name)
