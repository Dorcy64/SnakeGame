from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

SPEED = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score()

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

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.score += 1
        if SPEED > 0.4:
            SPEED -= 0.05
        score_board.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        stoppage += 1
        score_board.game_over()

    # Colision with Tail
    for segments in snake.segments[2:]:
        if snake.head.distance(segments) < 10:
            score_board.game_over()
            stoppage += 1

screen.exitonclick()