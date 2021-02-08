from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food

SPEED = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

stoppage = 0
while 1 > stoppage:
    screen.update()
    time.sleep(SPEED/10)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()