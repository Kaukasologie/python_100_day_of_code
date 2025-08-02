from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, "center", ("Courier", 16, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("Courier", 16, "bold"))

    def add_point(self):    #incresase_score
        self.score += 1
        self.clear()
        self.update_scoreboard()



