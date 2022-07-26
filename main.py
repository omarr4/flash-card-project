from tkinter import *
import pandas
import random

# Constants --------------------------------------------------------------------------------------------
words_df = pandas.read_csv("data/french_words.csv")

BACKGROUND_COLOR = "#B1DDC6"
TITLE = "Flash Card Game - Learn French!"
FONT_LANG = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
FRONT_IMG = "images/card_front.png"
BACK_IMG = "images/card_back.png"
RIGHT_IMG = "images/right.png"
WRONG_IMG = "images/wrong.png"

# Global Variables
french_word = ""
english_word = ""
to_learn = {row.French: row.English for (index, row) in words_df.iterrows()}

# you should add words to learn csv later
# this app can be used for you to memorize and learn different stuff, use it


# Functions --------------------------------------------------------------------------------------------
def got_right():
    global to_learn
    to_learn.pop(french_word)

    if len(to_learn) == 0:
        to_learn = {row.French: row.English for (index, row) in words_df.iterrows()}

    show_french()


def show_french():
    global french_word
    button_state("disabled")

    french_word = random.choice(list(to_learn))

    flip_card("French", french_word, img_front)
    window.after(3000, show_english)


def show_english():
    global english_word
    button_state("normal")

    english_word = to_learn[french_word]

    flip_card("English", english_word, img_back, "white")


def flip_card(lang, word, img, fill="black"):
    canvas.itemconfig(card_title, text=lang, fill=fill)
    canvas.itemconfig(card_word, text=word, fill=fill)
    canvas.itemconfig(img_canvas, image=img)


def button_state(state):
    wrong_btn['state'] = state
    right_btn['state'] = state


# UI ------------
# Window --------------------------------------------------------------------------------------------
window = Tk()
window.title(TITLE)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas --------------------------------------------------------------------------------------------
img_front = PhotoImage(file=FRONT_IMG)
img_back = PhotoImage(file=BACK_IMG)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_canvas = canvas.create_image(400, 263, image=img_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, font=FONT_LANG)
card_word = canvas.create_text(400, 263, font=FONT_WORD)

# Buttons --------------------------------------------------------------------------------------------
img_wrong = PhotoImage(file=WRONG_IMG)
wrong_btn = Button(image=img_wrong, highlightthickness=0, command=show_french)
wrong_btn.grid(row=1, column=0)

img_right = PhotoImage(file=RIGHT_IMG)
right_btn = Button(image=img_right, highlightthickness=0, command=got_right)
right_btn.grid(row=1, column=1)


show_french()

window.mainloop()
