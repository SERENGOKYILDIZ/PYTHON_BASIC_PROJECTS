from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#/---------------------------------------------- DATA READ ---------------------------------------------/
data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}
try:
    my_datas = pandas.read_csv("./data/words_to_learn.csv")
    learn_list = my_datas.to_dict(orient="records")
except FileNotFoundError:
    learn_list = []
    my_datas = pandas.DataFrame(learn_list)
    my_datas.to_csv("./data/words_to_learn.csv", index=False)
    learn_list = my_datas.to_dict(orient="records")
#/---------------------------------------------- FUNCTIONS ---------------------------------------------/
def known():
    global data, my_datas
    learn_list.append(current_card)
    to_learn.remove(current_card)

    my_datas = pandas.DataFrame(learn_list)
    my_datas.to_csv("./data/words_to_learn.csv", index=False)

    datas = pandas.DataFrame(to_learn)
    datas.to_csv("./data/french_words.csv", index=False)

    next_card()

def Not_known():
    next_card()
def next_card():
    global current_card, timer1
    window.after_cancel(timer1)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    timer1 = window.after(3000, func=show_card)

def show_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
#/---------------------------------------------- UI SETUP ----------------------------------------------/
window = Tk()

card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
my_right_img = PhotoImage(file="./images/right.png")
my_wrong_img = PhotoImage(file="./images/wrong.png")

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer1 = window.after(3000, func=show_card)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_btn = Button(image=my_wrong_img, highlightthickness=0, command=Not_known)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=my_right_img, highlightthickness=0, command=known)
right_btn.grid(column=1, row=1)

next_card()

window.mainloop()