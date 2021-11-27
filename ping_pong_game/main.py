#staring screen 600X800 

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
import random
from score_board import scoreBoard

#our main screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong game")
screen.tracer(0)

colors = ["grey", "cyan", "white", "blue", "pink", "yellow", "red", "green", "brown", "sky blue"]

#create paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = scoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while(game_is_on):
	time.sleep(0.05)
	screen.update()
	ball.move()

	#detect collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()
		ball.color(random.choice(colors))

	#detect collision with right paddle
	if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_x()
		ball.color(random.choice(colors))

	#detection of r_paddle missed ball
	if ball.xcor() > 360:
		ball.reset_position()
		score.l_point()
	#detection of l_paddle missed ball
	if ball.xcor() < -360:
		ball.reset_position()
		score.r_point()

screen.exitonclick()
