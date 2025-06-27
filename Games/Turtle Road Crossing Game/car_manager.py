from turtle import Turtle
import random

COLORS = ["red", "orange", "brown", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.my_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_cars(self):
        create_a_car = random.randint(1,6)
        if create_a_car == 1:
            all_cars = Turtle("square")
            all_cars.shapesize(stretch_wid=1,stretch_len=2)
            all_cars.penup()
            all_cars.color(random.choice(COLORS))
            rand_y = random.randint(-250,250)
            all_cars.goto(300,rand_y)
            self.my_cars.append(all_cars)
        
    def move_cars(self):
        for car in self.my_cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
            
        