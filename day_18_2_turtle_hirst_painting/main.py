from turtle import Turtle, Screen
import random
from extract_colors_from_picture import rgb_colors


RADIUS = 10
SPACED = 50
side = 10 * ((2 * RADIUS) + SPACED)     # 10 * (20 + 50) = 700
distance = SPACED + (2 * RADIUS)        # 50 + 20 = 70

timmy = Turtle()
screen = Screen()

timmy.shape("arrow")
timmy.speed("fastest")
screen.colormode(255)
screen.screensize(side, side)   # 700 x 700


def draw_circle(color):
    timmy.pendown()
    timmy.color(color)
    timmy.begin_fill()
    timmy.circle(RADIUS)
    timmy.end_fill()
    timmy.penup()


start_x = -1 * (side // 2) + (SPACED // 2) + RADIUS     # -350 + 25 + 10 = -315
start_y = -1 * (side // 2) + (SPACED // 2)              # -350 + 25 = - 325
prev_color = (0, 0, 0)

for y in range(10):
    timmy.teleport(start_x, start_y)
    for x in range(10):
        random_color = random.choice(rgb_colors)
        while prev_color == random_color:
            random_color = random.choice(rgb_colors)
        prev_color = random_color

        draw_circle(random_color)
        timmy.forward(distance)
    start_y += distance

timmy.hideturtle()
screen.exitonclick()
