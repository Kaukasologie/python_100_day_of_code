from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.shape("arrow")

screen = Screen()
screen.colormode(255)

angles_degree = 0

for angles_number in range (3, 11):
    angles_degree = 360 / angles_number
    timmy.color(randint(1, 255), randint(1, 255), randint(1, 255))
    for _ in range(angles_number):
        timmy.forward(100)
        timmy.right(angles_degree)

# def draw_shape(num_sides):    # function solution
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)

screen.exitonclick()
