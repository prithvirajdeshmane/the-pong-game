from turtle import Screen
from paddle import Paddle

""" Screen variables """
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = "black"
TITLE = "Pong"

""" Paddle variables """
XCOR_RIGHT_PADDLE = 350
XCOR_LEFT_PADDLE = -350

""" Game tracking variable"""
is_game_on = True

# create Game Screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(TITLE)
screen.tracer(0)

# create right paddle
right_paddle = Paddle(XCOR_RIGHT_PADDLE)
left_paddle = Paddle(XCOR_LEFT_PADDLE)

# set screen to listen for up and down arrow keys
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down, "s")

while is_game_on:
    screen.update()


screen.exitonclick()
