from turtle import Turtle, Screen
import random

screen = Screen()
colours = ['black', 'orange', 'red', 'violet', 'purple', 'blue', 'green']
y_pos = [-150, -100, -50, 0, 50, 100, 150]
race_on = False
screen.setup(width=700, height=500)
user_bet = screen.textinput(title="Make a Bet", prompt="Which turtle will win the race? Enter a colour : ")
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-325, y=y_pos[i])
    new_turtle.color(colours[i])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 330:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won the race! The {winning_color} colour turtle is the winner.")
            else:
                print(f"You have lost the race! The {winning_color} colour turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()