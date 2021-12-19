import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.onkey(player.move, "Up")

game_is_on = True
game_speed = 0.05
while game_is_on:
    car_manager.random_car()
    car_manager.move_cars()
    for car in car_manager.cars:
        if abs(car.xcor() - player.xcor()) < 22 and abs(car.ycor() - player.ycor()) < 22:
            scoreboard.print_game_over()
            game_is_on = False
    if player.ycor() > 290:
        player.respawn()
        scoreboard.increment_level()
        car_manager.reset_cars()
        game_speed *= 0.5
    screen.update()
    time.sleep(game_speed)

screen.exitonclick()
