FONT = ("Courier", 16, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-230,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.color("white")
        self.write(f"Level : {self.level}", move=False, align="center", font=FONT)

    def score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",move = False,align="center",font = ("Courier", 26, "normal"))