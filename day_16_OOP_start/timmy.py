from turtle import Screen
import turtle
import another_module


timmy = turtle.Turtle()                             # "Turtle()" - Class
print(timmy)

timmy.shape("turtle")
timmy.color("chartreuse")
timmy.forward(100)

my_screen = Screen()
canvas_height = my_screen.canvheight                # "canvheight" - variable from another file (module)
# variable = another_module.another_variable        # "another_variable" - variable from another_module

print(canvas_height)
# print(variable)

my_screen.exitonclick()
