from turtle import Turtle, Screen
screen = Screen()

ALIGNMENT = "center"
FONT = ('Arial', 20, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        try:
            with open("high-score.txt") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            with open("high-score.txt", mode="w") as hs:
                test = str(self.score)
                hs.write(test)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.create_scoreboard()

    def create_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)
        self.update_high_score_txt()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.create_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=('Arial', 20, 'bold'))

    def update_high_score_txt(self):
        if self.score > self.high_score:
            with open("high-score.txt", mode="w") as hs:
                test = str(self.score)
                hs.write(test)
        else:
            pass
