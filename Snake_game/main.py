from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import scoreBoard
import time

screen = Screen()
screen.setup(width =600, height =600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = scoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = Turtle
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()

	#detection with food
	if snake.head.distance(food) <15:
		food.refresh()
		snake.extend()
		score.increase_score()

	#detection with wall	
	if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
		score.reset_score()
		snake.reset_snake()

	#tail collision detection
	for segment in snake.segments:
		if segment == snake.head:
			pass
		elif snake.head.distance(segment) < 10:
			score.reset_score()

screen.exitonclick()
