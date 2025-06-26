from turtle import Turtle
ALIGNMENT ="center"
FONT = ("Courier", 14, "bold")
FONT_FOR_GAMEOVER = ("Courier", 18, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over ",align=ALIGNMENT,font=FONT_FOR_GAMEOVER)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        
