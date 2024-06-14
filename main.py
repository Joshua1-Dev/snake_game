from turtle import Turtle
import turtle
from turtle import Screen
import time
import snake
from snake import Snake
from food import Food
import scoreboard
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 420 or snake.head.xcor() < -420 or snake.head.ycor() > 420 or snake.head.ycor() < -420:
        game_is_on = False
        scoreboard.gameover()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()
            
        
screen.exitonclick()