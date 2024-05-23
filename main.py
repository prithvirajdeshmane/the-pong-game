from turtle import Screen
from paddle import Paddle

""" Screen variables """
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = "black"

""" Paddle variables """
XCOR_RIGHT_PADDLE = 350
XCOR_LEFT_PADDLE = -350

# create Game Screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Pong")


# create right paddle
right_paddle = Paddle(XCOR_RIGHT_PADDLE)

screen.exitonclick()