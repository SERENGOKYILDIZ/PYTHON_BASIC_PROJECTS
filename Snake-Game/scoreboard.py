from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 24, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as self.file:
            self.high_score = int(self.file.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score:{self.score} High Score:{self.high_score}", True, align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as self.file:
                self.file.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

