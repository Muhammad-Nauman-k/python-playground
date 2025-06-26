from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180 


class Snake:
#------------------------- Snake Body -------------------------------
    def __init__(self):

        self.snake_body =[]
        self.create_snake()
        self.head = self.snake_body[0]
        
    def create_snake(self):
        xs = 0
        for i in range(3):
            self.add_tail(position=(xs,0))
            xs -= 20
                
    #----------- Increase Size on eating Food ---------------------------
    def add_tail(self,position):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_body.append(snake)
            
    
    def extend(self):
        self.add_tail(self.snake_body[-1].position())
                
    
    #-------------------- Move the snake Body ---------------------------
    def move(self):
        for body in range(len(self.snake_body)-1, 0, -1):  #(Start,  Stop,  Step)   Stop is not included
                
            x_cor = self.snake_body[body - 1].xcor()
            y_cor = self.snake_body[body - 1].ycor() 
            self.snake_body[body].goto(x_cor,y_cor) 
            
        self.head.forward(MOVE_DISTANCE)
        
        
    
    #---- Movement ------
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
            
    
    
            
            
    #--------------------------------------------------------------------

