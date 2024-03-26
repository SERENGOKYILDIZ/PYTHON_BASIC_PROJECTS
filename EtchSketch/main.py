from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def onForward():
    timmy.forward(10)
def onBackward():
    timmy.backward(10)
def Clockwise():
    timmy.setheading(timmy.heading() - 10)
def Counter_Clockwise():
    timmy.setheading(timmy.heading() + 10)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(fun=onForward, key="w")
screen.onkey(fun=onBackward, key="s")
screen.onkey(fun=Clockwise, key="d")
screen.onkey(fun=Counter_Clockwise, key="a")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
