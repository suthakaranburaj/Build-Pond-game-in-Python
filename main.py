from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from random import Random
import time

screen=Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800,height=600)
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()


def display_winner(winner):
    winner_turtle = Turtle()
    winner_turtle.hideturtle()
    winner_turtle.color("white")
    winner_turtle.penup()
    winner_turtle.goto(0, 0)
    winner_turtle.write(f"{winner} Wins!", align="center", font=("Courier", 24, "normal"))

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on =True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x()
    # # if ball.xcor() > 380 or ball.xcor() < -380:
    # #     print("game over")
    #     game_is_on=False
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score >= 10:
        display_winner("Right Player ")
        game_is_on = False
    elif scoreboard.r_score >= 10:
        display_winner("Left Player")
        game_is_on = False


screen.exitonclick()