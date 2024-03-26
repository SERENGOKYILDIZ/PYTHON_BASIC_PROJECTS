import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("Ameriga Eyaletleri Bulma Oyunu")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0

is_play = True

data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
known_states = []
while len(known_states) < 50:
    secim = screen.textinput(title=f"{score}/50 Score var", prompt="Eyalet tahmininiz?").title()
    if secim == "Exit":
        new_dataFrame = pandas.DataFrame(known_states)
        new_dataFrame.to_csv("gameData.csv")
        break
    secim_state = data[data["state"] == secim]
    if secim_state.empty:
        continue
    var_mi = False
    for n in known_states:
        if n == secim:
            var_mi = True

    if var_mi:
        pass
    else:
        secim_x = float(secim_state["x"])
        secim_y = float(secim_state["y"])
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(secim_x, secim_y)
        new_turtle.write(secim, True, align="center", font=('Arial', 8, 'normal'))
        known_states.append(secim)
        score += 1