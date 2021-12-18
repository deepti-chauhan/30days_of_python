from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")



class scoreBoard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		with open("my_score.txt", mode = 'r') as file:
			self.high_score = int(file.read())
		self.color("white")
		self.penup()
		self.goto(0, 250)
		self.hideturtle()
		self.update()

	def update(self):
		self.clear()
		self.write(f"Score: {self.score} High Score {self.high_score}", align = ALIGNMENT, font=	FONT)

	def increase_score(self):
		self.score +=1
		self.update()

	def reset_score(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open("my_score.txt", mode='w') as file:
				int(file.write(f" {self.high_score}"))
		self.score = 0
		self.update() 

