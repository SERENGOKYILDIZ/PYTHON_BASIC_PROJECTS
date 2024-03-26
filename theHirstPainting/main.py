###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle

import colorgram
from turtle import Turtle, Screen
import random

myTurtle = Turtle()
colors=[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

myScreen = Screen()
myTurtle.penup()
turtle.colormode(255)
myTurtle.speed("fastest")
myTurtle.hideturtle()

for a in range(1,10):
    myTurtle.setposition(-225, -225+a*50)
    myTurtle.pos()
    for b in range(10):
        myTurtle.dot(20, random.choice(colors))
        myTurtle.forward(50)


myScreen.exitonclick()