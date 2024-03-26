from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.bodys = []
        self.create_snake()
        self.head = self.bodys[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position)
        self.bodys.append(new_body)

    def reset(self):
        for body in self.bodys:
            body.goto(1000, 1000)
        self.bodys.clear()
        self.create_snake()
        self.head = self.bodys[0]
    def extern(self):
        self.add_body(self.bodys[-1].position())

    def move(self):
        for body_num in range(len(self.bodys) - 1, 0, -1):
            new_x = self.bodys[body_num - 1].xcor()
            new_y = self.bodys[body_num - 1].ycor()
            self.bodys[body_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def onkey_w(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def onkey_a(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def onkey_s(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def onkey_d(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
