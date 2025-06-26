from turtle import Screen
from board_file import Paddle
from ball_file import Ball
from scoreboard_file import ScoreBoard
import time


#-------- Screen Setup -------------
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


R_paddle = Paddle((350,0))
L_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()

#----- Movement ---------
screen.listen()
screen.onkey(R_paddle.go_up,"Up") 
screen.onkey(R_paddle.go_down,"Down")
screen.onkey(L_paddle.go_up,"w") 
screen.onkey(L_paddle.go_down,"s")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #Detect Collision with Upper/Lower Wall
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect Collision with Paddle
    
    if ball.distance(R_paddle) < 50 and ball.xcor() > 320 or ball.distance(L_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Detect when the Right Side Paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    
    #Detect when the Left Side Paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
        
    










screen.exitonclick()