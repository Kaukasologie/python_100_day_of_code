from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setheading(45)
        self.move_speed = 0.005

    def move_ball(self):
        self.penup()
        self.forward(1)

    def change_y_direction(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def change_x_direction(self, x_cor):
        new_heading = 0
        # Why x coordinates?
        if x_cor <= 180:
            new_heading = 180 - self.heading()
        elif x_cor > 180:
            new_heading = 360 - self.heading() + 180

        self.move_speed *= 0.9
        self.setheading(new_heading)
        print(self.move_speed)

    def reset_ball(self):
        self.move_speed = 0.005
        self.change_x_direction(self.xcor())
        self.goto(0, 0)
