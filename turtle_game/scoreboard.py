
from turtle import Turtle

FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
	
	def __init__(self):
		super().__init__()
		self.level = 1
		self.hideturtle()
		self.penup()
		self.goto(-280, 260)
		self.score_update()

	def score_update(self):
		self.clear()
		self.write(f"Level: {self.level}", align="left", font=FONT)

	def update(self):
		self.level += 1
		self.score_update()

	def game_over(self):
		self.goto(0,0)
		self.write("GAME OVER", align="center", font = FONT)

