import random
from turtle import Turtle

COLORS = ["red", "yellow", "green", "blue", "purple","black"]
START_POSITION = 5
INCREMENT_MOVE = 10

class Manager:
	def __init__(self):
		self.all_cars =[]
		self.car_speed = START_POSITION

	def create_car(self):
		random_space = random.randint(1,6)
		if random_space == 1:
			new_car = Turtle("square")
			new_car.shapesize(stretch_wid =1, stretch_len =2)
			new_car.penup()
			new_car.color(random.choice(COLORS))
			random_y = random.randint(-250, 250)
			new_car.goto(300, random_y)
			self.all_cars.append(new_car)

	def move_car(self):
		for car in self.all_cars:
			car.backward(START_POSITION)

	def level_up(self):
		self.car_speed += INCREMENT_MOVE

