from turtle import Screen
import time
from Snake import Snake
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


game_on = True
snake = Snake()
food = Food()
score_board = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_on:

    screen.update()
    time.sleep(.1)
    snake.move()
    #score = 0
    if snake.head.distance(food) < 15:
        score_board.update()
        food.refresh()
        snake.extend()
    if snake.turtle_list[0].xcor()> 290 or snake.turtle_list[0].xcor()< -290 or snake.turtle_list[0].ycor()> 290 or snake.turtle_list[0].ycor()< -290:
        game_on = False
        score_board.game_over()

    for snek in snake.turtle_list[1: ]:
        # if snek == snake.head:
        #     pass
        if snake.head.distance(snek) < 5:
            game_on = False
            score_board.game_over()

screen.exitonclick()
