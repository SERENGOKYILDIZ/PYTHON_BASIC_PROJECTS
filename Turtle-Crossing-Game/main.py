import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.moveUp, key="w")

game_is_on = True

count = 0.0
timeout = random.random()

while game_is_on:
    time.sleep(0.1)
    screen.update()

    scoreboard.writeLabel()
    car_manager.moveCars()
    count += 0.06

    if count >= timeout:
        car_manager.Newcar()
        count = 0.0
        timeout = random.random()

    if player.ycor() > 260:
        scoreboard.add_level()
        car_manager.add_Speed()
        player.goto(0, -280)

    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.gameOver()
            game_is_on = False


screen.exitonclick()
