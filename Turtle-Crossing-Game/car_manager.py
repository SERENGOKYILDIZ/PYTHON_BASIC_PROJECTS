from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def creatingCar(self, ycor):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.goto(280, ycor)
        new_car.yeks = ycor
        self.cars.append(new_car)

    def Newcar(self):
        y = random.randint(-250, 250)
        self.creatingCar(y)

    def moveCars(self):
        for car in self.cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.yeks)
            self.checkWall(car)

    def checkWall(self, car):
        if car.xcor() <= -300:
            self.cars.remove(car)
            car.hideturtle()

    def add_Speed(self):
        self.speed += MOVE_INCREMENT
    pass
