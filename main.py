__author__ = "Vujic Dejan"

# Libaries
import tkinter as tk
from tkinter import *
from random import randint

class GuessingNumber(Frame):

    def __init__(self, master):
        # Initialization gui frame
        super(GuessingNumber, self).__init__(master) 
        # Set variables 
        self.description = StringVar()
        self.result = StringVar()
        self.chances = IntVar()
        self.chances1 = IntVar()
        self.choice = IntVar()


    def variables(self):
        # Set values
        self.description.set("Guess a number from 1 to 100 ")
        self.result.set("")
        self.chances.set(5)
        self.chances1.set(self.chances.get())

        # Set the secret number
        self.secret_number = randint(1, 100)
        print(self.secret_number)

    # Game logic functions
    def game(self):

        self.chances1.set(self.chances.get())
        if self.chances.get() > 0:

            if self.choice.get() > 100 or self.choice.get() < 0:
                self.result.set("You have exceeded the number limit. You lost 1 chance.")
                self.chances.set(self.chances.get() - 1)
                self.chances1.set(self.chances.get())

            elif self.secret_number == self.choice.get():
                self.result.set("Bravo! YOU WON")
                self.chances.set(self.chances.get() - 1)
                self.chances1.set(self.chances.get())

            elif self.secret_number > self.choice.get():
                self.result.set("Your number was less then secret number! \nTry again! ")
                self.chances.set(self.chances.get() - 1)
                self.chances1.set(self.chances.get())
            elif self.secret_number < self.choice.get():
                self.result.set(
                    "Your number was higher then secret number! \nTry again! ")
                self.chances.set(self.chances.get() - 1)
                self.chances1.set(self.chances.get())
        else:
            self.result.set(
                "GAME OVER! You lost")

    
    def restart(self):
        # Restart application
        self.secret_number = randint(1, 100)
        print(self.secret_number)

        self.description.set("Guess a number from 1 to 100")
        self.result.set("")
        self.chances.set(5)
        self.chances1.set(self.chances.get())

    # Create GUI widgets
    def create_widgets(self):
        desc_play_message = tk.Label(frame, text = "LET'S PLAY! ", bg="#065569", fg="#ffffff", font=("Helvetica", 24, 'bold'))
        desc_num_message = tk.Label(frame, textvariable = self.description, bg="#065569", fg="#ffffff", font=("Helvetica"))
        result_message = tk.Label(frame, textvariable = self.result, bg="#065569", fg="#ffffff", font=("Helvetica"))
        chances_message = tk.Label(frame, text = "Remaninig Chances: ", bg="#065569", fg="red", font=("Helvetica"))
        chances_values = tk.Label(frame, textvariable = self.chances1, bg="#065569", fg="red", font=("Helvetica"))


        desc_play_message.place(x = 220, y = 40)
        desc_num_message.place(x = 200, y = 100)
        result_message.place(x = 165, y = 130)
        chances_message.place(x = 215, y = 240)
        chances_values.place(x = 350, y = 240)

        entry_form = tk.Entry(frame, textvariable = self.choice, font = ("Helvetica"), bg = "#eaff7b")
        entry_form.place(x = 210, y = 180)

        play_button = tk.Button(frame, text = "Play game", highlightbackground = "green", font=("Helvetica", 24, "bold"),
                    command=self.game)
        restart_button = tk.Button(frame, text = "Restart game", font = ("Helvetica", 16, "bold"),
                    command=self.restart)
        exit_button = tk.Button(frame, text = "Exit game", highlightbackground = "red", font = ("Helvetica", 16, "bold"),
                    command = exit)

        play_button.place(x = 245, y = 315)
        restart_button.place(x = 90, y = 320)
        exit_button.place(x = 420, y = 320)

# Driver code

# GUI frame configuration
frame = tk.Tk()
frame.geometry("600x400")
frame.resizable(width = False, height = False)
frame.config(bg = "#065569")
frame.title("Guessing Number Game")

# Definition application
application = GuessingNumber(frame)
application.create_widgets()
application.variables()
application.game()
application.restart()
frame.mainloop()
