from turtle import Turtle
ALIGNMENT="center"
FONT=('joker', 24, 'normal')

class Score(Turtle):
    def __init__(self):

        self.scoreval =0

        with open("data", mode="r") as file:
            self.highscore = int(file.read())


        # file= open("data")
        # data=file.read()
        # self.data=int(data)
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.hideturtle()
        self.updatescore()
    def updatescore(self):
        self.clear()
        self.write(f"SCORE:{self.scoreval}  HIGH SCORE:{self.highscore}", align=ALIGNMENT, font=FONT)
    def currentscore(self):
        self.scoreval+=1
        self.clear()
        self.updatescore()
    def renew(self):
        if self.scoreval>self.highscore:
            self.highscore = self.scoreval
            with open("data", mode="w") as change:
                change.write(str(self.scoreval))
        self.scoreval=0
        self.updatescore()