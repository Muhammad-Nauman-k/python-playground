import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_cars()
    carmanager.move_cars()
    
    #Detect Collision with car
    for car in carmanager.my_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    #Detect if turtle is successful
    if player.is_successful():  # Turtle has crossed the road
        player.goto_start()          # Move Turtle to the start position      
        carmanager.level_up()        # Increase speed of cars on level up
        scoreboard.increase_level()
     
          
          
            
screen.exitonclick()