PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_txt:
    names_list = names_txt.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as template_file:
    template = template_file.read()
    for name in names_list:
        stripped_name = name.strip()
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as new_letter:
            new_letter.write(template.replace(PLACEHOLDER, stripped_name))
