from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class scoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("white")
		self.penup()
		self.goto(0, 250)
		self.hideturtle()
		self.update()

	def update(self):
		self.write(f"Score: {self.score}", align = ALIGNMENT, font=	FONT)

	def increase_score(self):
		self.score +=1
		self.clear()
		self.update()

	def game_over(self):
		self.goto(0,0)
		self.write("Gameover", align=ALIGNMENT, font=	FONT)
