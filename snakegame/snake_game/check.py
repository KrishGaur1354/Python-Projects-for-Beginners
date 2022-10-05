from turtle import Turtle , Screen
import time

screen= Screen()

screen.setup(width = 600,height=600)
screen.bgcolor("black")
screen.title("my game")
screen.tracer(0)
#  ye humne body bana li
body = [(0,0),(-20,0),(-40,0)]
segment=[]
for parts in body:
    moti = Turtle()
    moti.color("white")
    moti.shape("square")
    moti.penup()
    moti.goto(parts)
    segment.append(moti)


game_on = True
while game_on :
    screen.update()
    time.sleep(0.1)
    # ab snake ko turn karane ki liye hum ise ek tarike se link karenge iske co_ordinate se
    for seg in range (len(segment)-1,0,-1):
        new_xpos= segment[seg-1].xcor()
        new_ypos= segment[seg-1].ycor()
        segment[seg].goto(new_xpos,new_ypos)
    # ab hum first part ko control kar rahe hai aur pura snake control ho raha hai
    segment[0].forward(20)
    segment[0].left(90)




screen.exitonclick()
