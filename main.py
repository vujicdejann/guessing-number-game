__author__ = "Vujic Dejan"

# Libaries
import tkinter as tk
from tkinter import *
from random import randint

# GUI frame configuration
frame = tk.Tk()
frame.geometry("600x400")
frame.resizable(width = False, height = False)
frame.config(bg = "#065569")
frame.title("Guessing Number Game")

# Create variables for guess the number, results and remaining chances
description = StringVar()
result = StringVar()
chances = IntVar()
chances1 = IntVar()
choice = IntVar()

# Set the values
description.set("Guess a number from 1 to 100 ")
result.set("")
chances.set(5)
chances1.set(chances.get())

# Set the secret number
secret_number = randint(1, 100)
print(secret_number)

# Game logic functions
def game():
    chances1.set(chances.get())
    if chances.get() > 0:

        if choice.get() > 100 or choice.get() < 0:
            result.set("You have exceeded the number limit. You lost 1 chance.")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())

        elif secret_number == choice.get():
            result.set("Bravo! YOU WON")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())

        elif secret_number > choice.get():
            result.set("Your number was less then secret number! \nTry again! ")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())
        elif secret_number < choice.get():
            result.set(
                "Your number was higher then secret number! \nTry again! ")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())
    else:
        result.set(
            "GAME OVER! You lost")


def restart():
    global secret_number, description, result, chances, chances1

    secret_number = randint(1, 100)
    print(secret_number)
    description.set("Guess a number from 1 to 100")
    result.set("")
    chances.set(5)
    chances1.set(chances.get())


# Create GUI widgets
desc_play_message = tk.Label(frame, text = "LET'S PLAY! ", bg="#065569", fg="#ffffff", font=("Helvetica", 24, 'bold'))
desc_num_message = tk.Label(frame, textvariable = description, bg="#065569", fg="#ffffff", font=("Helvetica"))
result_message = tk.Label(frame, textvariable = result, bg="#065569", fg="#ffffff", font=("Helvetica"))
chances_message = tk.Label(frame, text = "Remaninig Chances: ", bg="#065569", fg="red", font=("Helvetica"))
chances_values = tk.Label(frame, textvariable = chances1, bg="#065569", fg="red", font=("Helvetica"))


desc_play_message.place(x = 220, y = 40)
desc_num_message.place(x = 200, y = 100)
result_message.place(x = 165, y = 130)
chances_message.place(x = 215, y = 240)
chances_values.place(x = 350, y = 240)

entry_form = tk.Entry(frame, textvariable = choice, font = ("Helvetica"), bg = "#eaff7b")
entry_form.place(x = 210, y = 180)

play_button = tk.Button(frame, text = "Play game", highlightbackground = "green", font=("Helvetica", 24, "bold"),
            command=game)
restart_button = tk.Button(frame, text = "Restart game", font = ("Helvetica", 16, "bold"),
            command=restart)
exit_button = tk.Button(frame, text = "Exit game", highlightbackground = "red", font = ("Helvetica", 16, "bold"),
            command = exit)

play_button.place(x = 245, y = 315)
restart_button.place(x = 90, y = 320)
exit_button.place(x = 420, y = 320)


frame.mainloop()
