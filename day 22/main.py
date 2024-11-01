from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboardpong import Score
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(key="Up",fun=r_paddle.up)
screen.onkey(key="Down",fun=r_paddle.down)
screen.onkey(key="w",fun=l_paddle.up)
screen.onkey(key="s",fun=l_paddle.down)


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor()>320 or ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>370:
        ball.reset_position()
        score.l_point()
    if ball.xcor()<-370:
        ball.reset_position()
        score.r_point()

screen.exitonclick()