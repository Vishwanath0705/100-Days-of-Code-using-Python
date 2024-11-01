from turtle import Turtle,Screen
from food import Food
from snake import Snake
from snakescore import Score
import time
screen = Screen()
screen.setup(800,800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        score.scoreup()

    if snake.head.xcor()>380 or snake.head.xcor()<-380 or snake.head.ycor()>340 or snake.head.ycor()<-380:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            score.reset()
            snake.reset()
screen.exitonclick()