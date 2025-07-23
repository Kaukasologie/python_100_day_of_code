from turtle import Turtle, Screen
from random import randint, choice

timmy = Turtle()
timmy.shape("arrow")

screen = Screen()

# timmy draw a line thicker than before
timmy.width(8)

# timmy draw faster than before
timmy.speed(7)

# “fastest”: 0
# “fast”: 10
# “normal”: 6
# “slow”: 3
# “slowest”: 1

# timmy pick a random color
screen.colormode(255)
# timmy.color(randint(1, 255), randint(1, 255), randint(1, 255))

# timmy choose and go in a random direction a random distance
angles = [0, 90, 180, 270]

while True:
    # timmy.right(choice(angles))

    # an alternative method that turns immediately:
    timmy.setheading(choice(angles))

    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    timmy.forward(30)
