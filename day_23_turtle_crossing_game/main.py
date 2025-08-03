import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(player.move, "w")
screen.onkeypress(player.move, "Up")

game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_over = True
            scoreboard.game_over()

    # Detect successful crossing
    if player.ycor() > 260:
        player.reset_position()
        scoreboard.update_scoreboard()
        car_manager.increase_speed()


screen.exitonclick()
