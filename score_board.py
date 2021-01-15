from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 260)
        self.score = 0
        self.write(f"SCORE {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE= {self.score}", align="center", font=("Arial", 24, "normal"))



