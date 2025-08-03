# TODO Fix bugs or completely rewrite the program
# The solution is different from the teacher's. Her movements are through changes in coordinates, mine are through setheading() and forward()

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

game_over = False

while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    #print(ball.heading())

    # Detection collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.change_y_direction()

    # Detection collision with paddles
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < - 330 and ball.distance(l_paddle) < 50:
         # Bug - When the ball hits the edge of the paddle it rolls along the paddle before bouncing and gains a lot of speed
         ball.change_x_direction(ball.xcor())

    # Detect R paddle misses
    if ball.xcor() > 370:
        ball.reset_ball()
        scoreboard.increase_l_point()
        speed = 0.005

    # Detect L paddle misses
    if ball.xcor() < -350:
        ball.reset_ball()
        scoreboard.increase_r_point()
        speed = 0.005

screen.exitonclick()
