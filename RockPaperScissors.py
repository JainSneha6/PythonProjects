from tkinter import *
import random

root = Tk()

root.geometry("1200x700")
root.title("Rock, Paper, Scissors")
root.config(bg="black")

rock = PhotoImage(file=r"RockPaperScissors\rock.png")
paper = PhotoImage(file=r"RockPaperScissors\paper.png")
scissors = PhotoImage(file=r"RockPaperScissors\scissors.png")

choices = ["rock", "paper", "scissors"]
label = None  


def game1():
    user_choice = "rock"
    display_result(user_choice)


def game2():
    user_choice = "paper"
    display_result(user_choice)


def game3():
    user_choice = "scissors"
    display_result(user_choice)


def display_result(user_choice):
    global label  
    computer_choice = random.choice(choices)

    if label:
        label.destroy()  

    if user_choice == computer_choice:
        result = "It's a TIE"
    elif (user_choice == "rock" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "rock"):
        result = "You LOSE"
    else:
        result = "You WIN"

    text = f'You choose {user_choice.capitalize()} while Computer chooses {computer_choice.capitalize()}.\n' \
           f"{result}!"

    label = Label(root, text=text, font="comicsans 25 bold", bg="black", fg="white")
    label.place(x=200, y=480)


header_frame = Frame(root, bg='black', height=60)
header_frame.pack(fill=X, padx=10, pady=10)

header_label = Label(header_frame, text="Rock, Paper, Scissors", font="comicsans 40 bold", bg='black', fg="white")
header_label.pack(pady=10)

rock_button = Button(root, image=rock, cursor="hand2", command=game1)
rock_button.place(x=80, y=150)

paper_button = Button(root, image=paper, cursor="hand2", command=game2)
paper_button.place(x=480, y=150)

scissors_button = Button(root, image=scissors, cursor="hand2", command=game3)
scissors_button.place(x=880, y=150)

root.mainloop()


