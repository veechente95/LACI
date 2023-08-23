from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip  # can copy text to clipboard automatically


def calculate_energy_rate():
    try:
        energy_used = float(energy_entry.get())
        total_energy = energy_used * 1.5
        result_label.config(text=f"Total Energy: {total_energy:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")


# -----UI SETUP -----#
window = Tk()
window.title("Energy Calculator")
window.config(padx=50, pady=50)

canvas = Canvas(height=300, width=400)
green_tech_image = PhotoImage(file="Images/green_tech.png")
canvas.create_image(200, 150, image=green_tech_image)
canvas.grid(column=1, row=0)

# Labels
energy_label = Label(text="Total Energy Used:")
energy_label.grid(column=0, row=1)
result_label = Label(text="", font=("Helvetica", 12, "bold"))
result_label.grid(column=1, row=2)

# Entries
energy_entry = Entry(width=15)
energy_entry.grid(column=1, row=1)
energy_entry.focus()

# Buttons
calculate_button = Button(text="Calculate Total Energy", command=calculate_energy_rate)
calculate_button.grid(column=2, row=1)

window.mainloop()
