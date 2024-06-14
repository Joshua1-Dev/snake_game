from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 400)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align= "center", font=("arial", 24, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write("gameover", align= "center", font=("arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def highscore(self):
        self.goto(200, 400)
        self.write(f"highscore:", align= "center", font=("arial", 24, "normal"))
