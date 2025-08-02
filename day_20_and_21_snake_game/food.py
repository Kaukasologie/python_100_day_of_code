from turtle import Turtle
import random

PERIMETR = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.color("white")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-PERIMETR, PERIMETR)
        random_y = random.randint(-PERIMETR, PERIMETR)
        self.goto(random_x, random_y)

