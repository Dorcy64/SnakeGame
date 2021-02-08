from turtle import Turtle, Screen
import time
from snake import Snake

SPEED = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

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


screen.exitonclick()