import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
player.goup()

car_manager = CarManager()
level_up = Scoreboard()

screen.listen()
screen.onkey(player.goup,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()
    for car in car_manager.all_cars:
        if car.distance(player)<30:
            game_is_on = False
            level_up.game_over()
    if player.is_at_finish():
        player.goto_start()
        car_manager.level_up()
        level_up.score()

screen.exitonclick()