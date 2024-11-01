from turtle import Turtle

pos = [(0,0),(-20,0),(-40,0)]
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in pos:
            self.add_segment(i)

    def add_segment(self,position):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
