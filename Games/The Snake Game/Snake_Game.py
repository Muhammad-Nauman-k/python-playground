from turtle import Screen
from Snake_Body_file import Snake
from food_file import Food
from scoreboard_file import ScoreBoard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  #Turn turtle animation on/off and set delay for update drawings

#----- Class Objects init -----
snake = Snake()
food = Food()
score = ScoreBoard()

#----- Listening to key strokes -----
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_is_on = True
while game_is_on:
    screen.update()   # Update the screen (Refesh the graphics) ( Work with screen.tracer L-25)
    time.sleep(0.1)
    
    snake.move()  
    
    # Detect Collision with Food
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        
    # Detect Collision with Wall
    x = snake.head.xcor()
    y = snake.head.ycor()
    if abs(x) > 280 or abs(y) > 280 :
        score.reset()
        snake.snake_reset()
        

    # Detect Collision with Tail
    for body in snake.snake_body[1:]:   #if body == snake.head:  (Skip the head)
        if snake.head.distance(body) < 10:
            score.reset()
            snake.snake_reset()
            
            
    
    
    
        
    






screen.exitonclick()