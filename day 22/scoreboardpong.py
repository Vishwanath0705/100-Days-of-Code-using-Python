from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,260)
        self.write(f"Score : {self.l_score}",move=False,align = "center",color = "white",font=("arial",16,"normal"))
        self.goto(100, 260)
        self.write(f"Score : {self.r_score}", move=False, align="center", font=("arial", 16, "normal"))

    def l_point(self):
        self.l_score+=1
        self.update_score()

    def r_point(self):
        self.r_score+=1
        self.update_score()