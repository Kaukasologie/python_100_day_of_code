from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

PERIMETR = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")

game_over = False

current_score = 0

while not game_over:
    screen.update()
    time.sleep(0.25)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_point()

    # Detect collision with wall
    if (snake.head.xcor() > PERIMETR or snake.head.xcor() < -PERIMETR
            or snake.head.ycor() > PERIMETR or snake.head.ycor() < -PERIMETR):

        game_over = True
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            score.game_over()



screen.exitonclick()
