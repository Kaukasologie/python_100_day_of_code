from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

data_file = ""
current_card = {}

# ---------------------------- CREATE CARD ------------------------------- #
try:
    data_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data_file = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = data_file.to_dict(orient="records")


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(background_image, image=card_front_background)
    canvas.itemconfig(card_word, text=f"{current_card["French"]}", fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    flip_timer = window.after(3000, func=change_card)


def change_card():
    canvas.itemconfig(background_image, image=card_back_background)
    canvas.itemconfig(card_word, text=f"{current_card["English"]}", fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")


def card_know():
    global current_card
    to_learn.remove(current_card)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv(path_or_buf="data/words_to_learn.csv", index=False)
    next_card()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)

flip_timer = window.after(3000, func=change_card)

card_front_background = PhotoImage(file="images/card_front.png")
card_back_background = PhotoImage(file="images/card_back.png")

#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background_image = canvas.create_image(400, 261, image=card_front_background)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

#Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=card_know)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
