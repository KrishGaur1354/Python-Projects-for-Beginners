import turtle

colors=["red" , "orange" , "yellow" , "green" , "blue" ,"indigo" , "violet" ]
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
for x in range(360):
    t.pencolor(colors[x%7])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)
