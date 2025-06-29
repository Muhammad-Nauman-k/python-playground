from turtle import Turtle
ALIGNMENT ="center"
FONT = ("Courier", 14, "bold")
FONT_FOR_GAMEOVER = ("Courier", 18, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score_file()
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)
        
    def high_score_file(self):
        with open("data.txt",mode="r") as file:
            self.high_score = int(file.read())                        
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
        
        self.score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_score()
        
