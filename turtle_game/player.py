from turtle import Turtle
START_POSITION = (0,-280)
DISTANCE_MOVE = 10
FINISH_LINE = 200


class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("turtle")
		self.penup()
		self.go_to_start()
		self.setheading(90)

	def go_up(self):
		self.forward(DISTANCE_MOVE)	

	def go_down(self):
		self.backward(DISTANCE_MOVE)

	def go_to_start(self):
		self.goto(START_POSITION)

	def at_finish_line(self):
		if self.ycor() > FINISH_LINE:
			return True
		else:
			return False

