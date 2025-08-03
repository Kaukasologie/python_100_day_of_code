from tkinter import *

def miles_to_km():
    miles = float(miles_entry.get())
    km = round(miles * 1.609347218694, 1)
    kilometer_result_label.config(text=km)

FONT = ("Arial", 11, "normal")
PADDING = 4

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=80)
window.config(padx=40, pady=20)

miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0, padx=PADDING, pady=PADDING)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0, padx=PADDING, pady=PADDING)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1, padx=PADDING, pady=PADDING)

kilometer_result_label = Label(text="0", font=("Arial", 12, "bold"))
kilometer_result_label.grid(column=1, row=1, padx=PADDING, pady=PADDING)

kilometer_label = Label(text="Km", font=FONT)
kilometer_label.grid(column=2, row=1, padx=PADDING, pady=PADDING)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2, padx=PADDING, pady=PADDING)


window.mainloop()
