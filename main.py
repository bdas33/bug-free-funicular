from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color")


color_list = ["blue", "red", "green", "yellow", "pink"]
cord_y = [0, 30, 60, -30, -60]
turtles = []

game_over = True
for x in range(5):
    tim = Turtle("turtle")
    tim.pu()
    tim.color(color_list[x])
    tim.goto(x=-230, y=cord_y[x])
    turtles.append(tim)

if user_bet:
    game_over = False


while not game_over:

    for tim in turtles:
        rand_move = random.randint(0, 10)
        tim.forward(rand_move)




# def move_forward():
#     tim.forward(10)
#
# def move_back():
#
#     tim.backward(10)
#
#
# def turn_right():
#     tim.rt(5)
#
#
# def turn_left():
#     tim.lt(5)
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)


screen.exitonclick()
