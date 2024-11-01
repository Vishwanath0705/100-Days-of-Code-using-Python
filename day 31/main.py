from tkinter import *
import pandas
import random

current_card = {}
to_learn = {}
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("flash-card-project-start/data/french_words_1.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,Text = "French", fill="black")
    canvas.itemconfig(card_word,Text = current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=logo_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, Text="English",fill="white")
    canvas.itemconfig(card_word, Text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=logo_back)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("flash-card-project-start/data/words_to_learn.csv", index=False)
    next_card()

"""window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
logo_front = PhotoImage(file="flash-card-project-start/images/card_front.png")
logo_back = PhotoImage(file="flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400, 263, image=logo_front)
card_title = canvas.create_text(400,150,text="",font=("Arial",23,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Arial",23,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

cross_image = PhotoImage(file="flash-card-project-start/images/wrong.png")
wrong_button = Button(image=cross_image,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)

correct_button = PhotoImage(file="flash-card-project-start/images/right.png")
right_button = Button(image=correct_button,highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)

next_card()

window.mainloop()"""
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
logo_front = PhotoImage(file="flash-card-project-start/images/card_front.png")
logo_back = PhotoImage(file="flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400, 263, image=logo_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="flash-card-project-start/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="flash-card-project-start/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

window.mainloop()