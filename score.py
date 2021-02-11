from turtle import Turtle

FONT = ("Arial", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)

        f = open("data.txt", mode="r")
        contents = int(f.read())
        self.high_score = contents
        f.close()

        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shapesize(1, 1)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.speed("fast")
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
        self.score = 0
        f = open("data.txt", mode="w")
        f.write(str(self.high_score))
        f.close()
        self.update_scoreboard()

