from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip  # can copy text to clipboard automatically


# def calculate_energy_rate():


# -----UI SETUP -----#
window = Tk()
window.title("Water & Power Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=300, width=400)
green_tech_image = PhotoImage(file="Images/green_tech.png")
canvas.create_image(200, 150, image=green_tech_image)  # cut (x,y) by half to center
canvas.grid(column=1, row=0)


# Labels
energy_used = Label(text="Energy used")
energy_used.grid(column=0, row=1)
email_label = Label(text="Email / Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()  # focuses to this entry to start typing right away when launched
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "test@gmail.com")  # inserts prepopulated text (0 for start, END for end of another text)
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# Buttons
#  = Button(text="Generate Password", command=)
# .grid(column=2, row=3)
#  = Button(text="Add", width=38, command=save)
# .grid(column=1, row=4, columnspan=2)


window.mainloop()
