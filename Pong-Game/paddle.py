from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.position = position_x
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position_x, 0)
        self.speed = 40

    def onUp(self):
        new_y = self.ycor() + self.speed
        self.goto(self.position, new_y)

    def onDown(self):
        new_y = self.ycor() - self.speed
        self.goto(self.position, new_y)
