from turtle import Turtle

FONT = ("Arial", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shapesize(1, 1)
        self.refresh()



    def refresh(self):
        self.speed("fast")
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center",font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)