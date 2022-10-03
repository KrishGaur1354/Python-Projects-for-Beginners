from turtle import Turtle
import random
# ab hum turtle class inherit karenge
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.newfood()
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
    def newfood(self):
        self.penup()
        xcor= random.randint(-280,280)
        ycor= random.randint(-280,280)
        self.goto(xcor,ycor)
