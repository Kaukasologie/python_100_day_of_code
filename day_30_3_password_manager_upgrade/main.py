from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    gen_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, gen_password)
    pyperclip.copy(gen_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    website = website_entry.get().title()
    password = password_entry.get()
    email_or_username = email_username_entry.get()
    new_data = {
        website: {
            "email": email_or_username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email_or_username) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any field empty.")
    else:
        try:
            with open("data.json", "r", encoding="utf-8") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w", encoding="utf-8") as data_file:
                json.dump(new_data, data_file, ensure_ascii=False, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w", encoding="utf-8") as data_file:
                # Saving update data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Login: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not found", message="No details for the website exits.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()   # == Screen() class from turtle module
window.title("Password Manager")
window.config(padx=30, pady=30)

# Canvas
canvas = Canvas(width=120, height=200)
logo_image = PhotoImage(file="logo.png")    # file!
canvas.create_image(60, 100, image=logo_image)     # image!
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_username_entry = Entry(width=40)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "deutschlandiyalda@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(row=1, column=2)
password_generate_button = Button(text="Generate Password", command=generate_password, width=15)
password_generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=34, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
