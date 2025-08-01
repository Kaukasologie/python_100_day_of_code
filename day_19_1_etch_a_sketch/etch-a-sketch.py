from turtle import Turtle, Screen

rafael = Turtle()
screen = Screen()

def move_forward():
    rafael.forward(10)

def move_backward():
    rafael.back(10)

def clockwise():
    rafael.right(10)

def counter_clockwise():
    rafael.left(10)

def clear():
    rafael.clear()
    rafael.teleport(0, 0)
    rafael.setheading(0)


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
