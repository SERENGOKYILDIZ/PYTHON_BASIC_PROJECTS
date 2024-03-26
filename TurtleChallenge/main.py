import turtle
from turtle import Turtle, Screen
from random import *

colours = ["mediumblue", "darkgreen", "red", "yellow", "brown", "black", "wheat", "gray", "purple", "khaki", "lightSlateGray", "tan", "lime"]
yonler = [0, 90, 180, 270]

myTurtle = Turtle()
myTurtle.shape("turtle")
myScreen = Screen()

def random_Color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_Square():
    for _ in range(4):
        myTurtle.forward(100)
        myTurtle.right(90)


def draw_Dashed_Line():
    for _ in range(15):
        myTurtle.forward(10)
        myTurtle.penup()
        myTurtle.forward(10)
        myTurtle.pendown()


def draw_pol(sides):
    n = 3
    while n <= sides:
        myTurtle.color(choice(colours))
        ang = 360 / n
        for _ in range(n):
            myTurtle.forward(100)
            myTurtle.right(ang)
        n += 1

def random_walk():
    myTurtle.pensize(15)
    myTurtle.speed("fastest")
    turtle.colormode(255)

    for _ in range(200):
        myTurtle.setheading(choice(yonler))
        myTurtle.color(random_Color())
        myTurtle.forward(30)


def draw_spirograph(size_og_gap):
    myTurtle.speed("fastest")
    turtle.colormode(255)
    for _ in range(int(360 / size_og_gap)):
        myTurtle.color(random_Color())
        myTurtle.circle(100)
        myTurtle.setheading(myTurtle.heading() + size_og_gap)


# draw_Square()
# draw_Dashed_Line()
# draw_pol(10)
# random_walk()
# draw_spirograph(10)



myScreen.exitonclick()