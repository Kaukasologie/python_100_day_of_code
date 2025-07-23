from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.shape("square")

screen = Screen()
screen.colormode(255)

for i in range(4):
    timmy.color(randint(1, 255), randint(1, 255), randint(1, 255))
    timmy.forward(100)
    timmy.right(90)

screen.exitonclick()
