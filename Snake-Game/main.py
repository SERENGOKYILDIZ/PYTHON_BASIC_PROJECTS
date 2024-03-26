from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

mySnake = Snake()

screen.listen()
screen.onkey(fun=mySnake.onkey_w, key="w")
screen.onkey(fun=mySnake.onkey_s, key="s")
screen.onkey(fun=mySnake.onkey_a, key="a")
screen.onkey(fun=mySnake.onkey_d, key="d")

game_is_on = True

food = Food()
scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    mySnake.move()

    #Yemeğe çarpmayı algılama
    if mySnake.head.distance(food) < 15:
        food.refresh()
        mySnake.extern()
        scoreboard.add_score()

    #Duvara çarpmayı algılama
    if mySnake.head.xcor() > 280 or mySnake.head.xcor() < -280 or mySnake.head.ycor() > 280\
            or mySnake.head.ycor() < -280:
        scoreboard.reset()
        mySnake.reset()

    #Kuyruğa çarpışmayı algıla
    for body in mySnake.bodys[1:]:
        if mySnake.head.distance(body) < 10:
            scoreboard.reset()
            mySnake.reset()
screen.exitonclick()