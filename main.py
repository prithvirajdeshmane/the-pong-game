from turtle import Screen
from paddle import Paddle
from ball import Ball
import random
import time

""" Screen variables """
WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = "black"
TITLE = "Pong"

""" Paddle variables """
XCOR_RIGHT_PADDLE = 350
XCOR_LEFT_PADDLE = -350

# create Game Screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(TITLE)
screen.tracer(0)

# create right paddle
right_paddle = Paddle(XCOR_RIGHT_PADDLE)
left_paddle = Paddle(XCOR_LEFT_PADDLE)

# create ball
ball = Ball()

# set random initial heading for the ball
random_initial_heading = random.randint(-45, 45)
if random_initial_heading < 0:
    random_initial_heading = 360 - random_initial_heading

# set screen to listen for up and down arrow keys
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

""" Game tracking variable"""
is_game_on = True

while is_game_on:
    screen.update()
    ball.move(random_initial_heading)
    time.sleep(0.02)

    # detect collision with right paddle


    # detect collision with top wall


    #detect collision with bottom wall



screen.exitonclick()
