from turtle import Turtle, Screen
import random



is_race = False
screen = Screen()
screen.setup(500, 400)
secim = screen.textinput("Renk Secimi", "Hangi rengi tutuyorsunuz? :")
colors=["blue", "green", "orange", "yellow", "purple", "red"]
turtles=[]
for a in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[a])
    new_turtle.penup()
    new_turtle.goto(-230, a * 30 - 70)
    turtles.append(new_turtle)

if secim:
    is_race = True

while is_race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == secim:
                print(f"Sen kazandin! {secim} sectin {winning_color} kazandi")
            else:
                print(f"Kaybettin :( {secim} sectin {winning_color} kazandi")
            screen.bye()

        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
