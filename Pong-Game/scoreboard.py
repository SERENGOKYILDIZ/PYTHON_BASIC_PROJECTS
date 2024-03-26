from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.firstScore = 0
        self.secondScore = 0

        self.WriteScore()

    def WriteScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.firstScore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.secondScore, align="center", font=("Courier", 80, "normal"))

    def add_First(self):
        self.firstScore += 1
        self.WriteScore()

    def add_Second(self):
        self.secondScore += 1
        self.WriteScore()