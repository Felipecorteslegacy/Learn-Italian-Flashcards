from tkinter import *
import random
import pandas as pd

# ------------------------------------- Data Loading -------------------------------------
current_card = {}
data_dict = {}

try:
    data = pd.read_csv("./data/Words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("italian_translate.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


# ------------------------------------- Functions -------------------------------------
def change_word():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(data_dict)
    selected_word = current_card["it"]
    canvas.itemconfig(card_title, text="Italian", fill="black")
    canvas.itemconfig(card_word, text=selected_word, fill="black")
    canvas.itemconfig(canvas_image, image=image_front)
    timer = window.after(3000, time_changes)


def time_changes():
    canvas.itemconfig(card_title, text="Spanish", fill="white")
    canvas.itemconfig(card_word, text=current_card["es"], fill="white")
    canvas.itemconfig(canvas_image, image=image_back)


def is_known():
    data_dict.remove(current_card)
    data_1 = pd.DataFrame(data_dict)
    data_1.to_csv("./data/Words_to_learn.csv", index=False)
    change_word()


# ------------------------------------- UI/UX -------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Ariel", 40, "italic")
FONT_2 = ("Ariel", 60, "bold")

window = Tk()
window.title("Italian Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, time_changes)

# Images loaded

image_front = PhotoImage(file="./images/card_front.png")
image_back = PhotoImage(file="./images/card_back.png")
correct = PhotoImage(file="./images/right.png")
incorrect = PhotoImage(file="./images/wrong.png")

# Canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=image_front)
canvas.grid(row=0, column=0, columnspan=2)

# Canvas Text
title_label = card_title = canvas.create_text(400, 150, text="Title", font=FONT_1)
word_label = card_word = canvas.create_text(400, 263, text="word", font=FONT_2)

# Buttons

right_button = Button(image=correct, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)

wrong_button = Button(image=incorrect, highlightthickness=0, command=change_word)
wrong_button.grid(row=1, column=1)

change_word()

window.mainloop()
