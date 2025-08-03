from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-290, 270)
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"level: {self.level}", False, "left", FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", FONT)
