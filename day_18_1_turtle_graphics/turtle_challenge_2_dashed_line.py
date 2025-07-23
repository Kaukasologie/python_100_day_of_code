from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("triangle")

screen = Screen()
screen.colormode(255)

for i in range(20):
    timmy.pendown()
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)

screen.exitonclick()
