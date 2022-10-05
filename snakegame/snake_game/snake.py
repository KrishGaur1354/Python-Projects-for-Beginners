#ab hum snake ki class banaenge jo humar acoe tidy kar degi
from turtle import Turtle
BODY = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SHAPE="square"
COLOR="white"
class Snake :
    def __init__(self):
        self.segment=[]
        self.createsnake()
        self.head = self.segment[0]

    def createsnake(self):
        for parts in BODY:
            self.addseg(parts)
    def new(self):
        for i in self.segment:
            i.goto(700,700)
        self.segment.clear()
        self.createsnake()
        self.head = self.segment[0]
    def addseg(self,parts):
        # is wale function se segment add ho rahe hai
        moti = Turtle()
        moti.color(COLOR)
        moti.shape(SHAPE)
        moti.penup()
        moti.goto(parts)
        self.segment.append(moti)
    def extend(self):
        self.addseg(self.segment[-1].position())
    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_xpos = self.segment[seg - 1].xcor()
            new_ypos = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_xpos, new_ypos)
        self.head.forward(STEP)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


