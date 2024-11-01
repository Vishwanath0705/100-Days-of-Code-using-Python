from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("textfile.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.goto(-10, 370)
        self.color("white")
        self.write(f"Score : {self.score} High Score : {self.highscore}", move=False, align="center", font=("arial", 16, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("textfile.txt",mode = "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.increase_score()

    def scoreup(self):
        self.score+=1
        self.increase_score()

    """def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over",move = False,align="center",font = ("arial",24,"normal"))"""

