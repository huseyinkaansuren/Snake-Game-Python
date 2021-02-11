import turtle as t
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#1.CREATE A SNAKE BODY
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.update()
#3.CONTROL THE SNAKE
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # 0.1 second delay
    # 2.MOVE THE SNAKE
    snake.move()
    #4.DETECT COLLISION WITH FOOD
    if snake.head.distance(food)< 15:#Checking food with snake's head
        food.refresh()
        snake.extend()
        # 5.CREATE SCORE BOARD
        scoreboard.increase_score()
    #6.DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    #7.DETECT COLLISION WITH TAIL
    for segment in snake.snake_list[1:]:#without head****
        # if head collide with any part of snake:
        if snake.head.distance(segment) < 10:
        #trigger game_over
            scoreboard.game_over()
screen.exitonclick()