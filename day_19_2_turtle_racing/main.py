from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will in the race: red, orange, yellow, green, blue or purple?"
                                                          "\nEnter a color: ")

def turtles_attributes(new_color, new_y, turtles_list):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(new_color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=new_y)
    turtles_list.append(new_turtle)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = 130

for color in colors:
    turtles_attributes(color, y, all_turtles)
    y -= 50

if user_bet:
    is_race_on = True

text_output = Turtle()
text_output.hideturtle()

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            text_output.color(winning_color)

            if winning_color == user_bet:
                text_output.write(f"You've won! The {winning_color} turtle is winner!", align="center", font=("Arial", 10, "bold"))
            else:
                text_output.write(f"You've lost! The {winning_color} turtle is winner!", align="center", font=("Arial", 10, "bold"))

        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()
