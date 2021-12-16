import time
from turtle import Screen
from player import Player
from car_manager import Manager
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = Manager()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")


game_is_on = True
while game_is_on:
	time.sleep(0.1)
	screen.update()

	car_manager.create_car()
	car_manager.move_car()

	#detect collision with car
	for car in car_manager.all_cars:
		if car.distance(player) < 20:
			game_is_on = False
			score_board.game_over()

	#detect success : player has reached finish line
	if player.at_finish_line():
		player.go_to_start()
		car_manager.level_up()
		score_board.update()

screen.exitonclick()
