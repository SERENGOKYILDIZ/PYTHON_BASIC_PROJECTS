from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

firstPaddle = Paddle(-350)
secondPaddle = Paddle(350)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=firstPaddle.onUp, key="w")
screen.onkey(fun=firstPaddle.onDown, key="s")
screen.onkey(fun=secondPaddle.onUp, key="Up")
screen.onkey(fun=secondPaddle.onDown, key="Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(secondPaddle) < 50 and ball.xcor() > 320 or ball.distance(firstPaddle) < 50 and ball.xcor() < -320:
        ball.bouncePaddle()

    if ball.xcor() > 380:
        ball.resetMove()
        scoreboard.add_First()

    if ball.xcor() < -380:
        ball.resetMove()
        scoreboard.add_Second()

screen.exitonclick()