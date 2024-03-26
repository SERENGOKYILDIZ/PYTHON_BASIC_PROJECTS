from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1

    def add_level(self):
        self.level += 1

    def writeLabel(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
