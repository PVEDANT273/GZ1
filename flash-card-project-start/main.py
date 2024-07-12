from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("data/words_to_learn.csv", index_col=False)
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv", index_col=False)
    words_to_learn = data.to_dict(orient="records")
# parameter needed, because without it we don't get a proper list of dictionary
else:
    words_to_learn = data.to_dict(orient="records")
pulled_card = {}

def generate_word():
    global pulled_card
    global delay
    window.after_cancel(delay)
    pulled_card = random.choice(words_to_learn)
    french_word = pulled_card["French"]
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(title, text="French", fill="Black")
    canvas.itemconfig(word, text=french_word, fill="Black")
    delay = window.after(3000, change_slide)


def remove_word():
    words_to_learn.remove(pulled_card)
    print(len(words_to_learn))
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()

def change_slide():
    english_word = pulled_card["English"]
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")
    canvas.itemconfig(canvas_image, image=back_image)


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

delay = window.after(3000, change_slide)

check_image = PhotoImage(file="images/right.png")
cross_image = PhotoImage(file="images/wrong.png")
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=front_image)
title = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

check_button = Button(image=check_image, highlightthickness=0, command=remove_word)
check_button.grid(row=1, column=0)

cross_button = Button(image=cross_image, highlightthickness=0, command=generate_word)
cross_button.grid(row=1, column=1)

generate_word()

window.mainloop()
