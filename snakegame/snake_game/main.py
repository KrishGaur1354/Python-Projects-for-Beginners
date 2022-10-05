from turtle import Turtle , Screen
import time
from snake import Snake
from food import Food
from scorecard import Score
screen= Screen()
score=Score()

screen.setup(width = 600,height=600)
screen.bgcolor("black")
screen.title("my game")
screen.tracer(0)

snake =Snake()
food =Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on :
    screen.update()
    time.sleep(0.1)
    snake.move()
    #now to detect the collision
    if snake.head.distance(food)<15:
        food.newfood()
        snake.extend()
        score.currentscore()
    # collision with the tail
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.renew()
        snake.new()


    # collision with the tail
    for i in snake.segment[1:]:
        if i == snake.head:
            pass
        elif snake.head.distance(i)<10:
            score.renew()
            snake.new()




screen.exitonclick()