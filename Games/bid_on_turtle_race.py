import turtle
from turtle import Turtle, Screen
import random as r

# Set up turtle environment
turtle.colormode(255)
screen = Screen()
screen.setup(width=500, height=400)

# Get user input
user_bet = screen.textinput("Place Your Bet", "Which color turtle will win the race? ")

colors = ['red', 'purple', 'green', 'blue', 'orange', 'brown']
turtles = []

# Create turtles and position them on the left
start_y = -50
for turtle_index in range(6):
    racer = Turtle(shape="turtle")
    racer.color(colors[turtle_index])
    racer.penup()
    racer.goto(-230, start_y)
    turtles.append(racer)
    start_y += 30

# Start race if user entered a bet
if user_bet:
    is_on = True

winner = None  # To avoid unbound error
while is_on:
    for tt in turtles:
        if tt.xcor() > 230:
            winner = tt.pencolor()
            is_on = False
            break
        rand_dis = r.randint(0, 10)
        tt.forward(rand_dis)

# Declare result
if user_bet == winner:
    print(" Congratulations! You won the bet :) ")
else:
    print(f" You lost the bet :(  . The winner was {winner}.")

screen.exitonclick()
