from turtle import Turtle, Screen
from random import randint

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

def draw_circle(angle):
    timmy.left(angle)
    timmy.circle(100)
    timmy.setheading(0)

timmy = Turtle()
timmy.shape("arrow")

screen = Screen()
screen.colormode(255)

timmy.speed(0)

for angles in range (0, 361, 5):
    timmy.color(random_color())
    draw_circle(angles)

# Angela's solution

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)

screen.exitonclick()
